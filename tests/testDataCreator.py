import unittest
from unittest.mock import patch, mock_open, MagicMock
import json
import backend.dataCreator as dataCreator
import datetime

class TestDataCreator(unittest.TestCase):

    @patch("backend.dataCreator.getERData")
    def test_getPlayerNum(self, mock_getERData):
        mock_getERData.return_value = {"user": {"userNum": 12345}}
        result = dataCreator.getPlayerNum("TestPlayer")
        self.assertEqual(result, 12345)

    @patch("backend.dataCreator.getERData")
    def test_getPlayerData(self, mock_getERData):
        mock_getERData.side_effect = [
            {"userStats": [{"mmr": 2000, "totalGames": 10, "totalWins": 5, "characterStats": [{"characterCode": 1, "usages": 5}]}]}
        ]
        dataCreator.playerIDs = {"TestPlayer": {"id": 12345, "twitch": "test_twitch"}}
        result = dataCreator.getPlayerData("TestPlayer")
        self.assertEqual(result["playerName"], "TestPlayer")
        self.assertEqual(result["playerMMR"], 2000)
        self.assertEqual(result["playerWinRate"], 50)
        self.assertEqual(result["playerCharacterStats"][0]["playerCharacterCode"], "Jackie Mini")

    @patch("builtins.open", new_callable=mock_open, read_data='{"TestPlayer": {"id": 12345}}')
    @patch("json.dump")
    def test_saveDataToJson(self, mock_json_dump, mock_open_file):
        data = {"key": "value"}
        dataCreator.saveDatatoJson(data, "test.json")
        mock_open_file.assert_called_once_with("test.json", "w")
        mock_json_dump.assert_called_once_with(data, mock_open_file(), indent=4)

    @patch("backend.dataCreator.pytz.timezone")
    @patch("backend.dataCreator.datetime")
    @patch("builtins.open", new_callable=mock_open)
    @patch("json.dump")
    def test_saveCurrentTime(self, mock_json_dump, mock_open_file, mock_datetime,mock_timezone):
        mock_timezone.return_value = None

        mock_now = datetime.datetime(2023, 10, 1, 14 , 30)
        mock_datetime.datetime.now.return_value = mock_now
        dataCreator.saveCurrentTime()
        mock_open_file.assert_called_once_with("../data/last_updated.json", "w")
        mock_json_dump.assert_called_once()

    def test_sortPlayers(self):
        playerIDs = {
            "Player1": {"locked": False},
            "Player2": {"locked": True, "lockedRank": 1},
            "Player3": {"locked": False},
            "Player4": {"locked": True, "lockedRank": 2}
        }
        allPlayerData = [
            {"playerName": "Player1", "playerMMR": 1500},
            {"playerName": "Player2", "playerMMR": 200},
            {"playerName": "Player3", "playerMMR": 1800},
            {"playerName": "Player4", "playerMMR": 1000}
        ]
        sortedPlayers = dataCreator.sortPlayers(playerIDs, allPlayerData)

        self.assertEqual(sortedPlayers[0]["playerName"], "Player3") # 1800
        self.assertEqual(sortedPlayers[1]["playerName"], "Player1") # 1500
        self.assertEqual(sortedPlayers[2]["playerName"], "Player2") # locked rank > mmr sorting
        self.assertEqual(sortedPlayers[3]["playerName"], "Player4") # locked rank > mmr sorting

if __name__ == "__main__":
    unittest.main()