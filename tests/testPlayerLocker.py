import unittest
from unittest.mock import patch, mock_open
import json
from backend.playerLocker import unlockAllPlayer, lockLowestPlayer

class TestPlayerLocker(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='{"Player1": {"locked": true, "lockedRank": 1}, "Player2": {"locked": false, "lockedRank": null}}')
    @patch("json.dump")
    def test_unlockAllPlayer(self, mock_json_dump, mock_open_file):
        with open("../web/data/player_ID.json", "r") as file:
            player_data = json.load(file)

        unlockAllPlayer(player_data)
        for player in player_data.values():
            self.assertFalse(player["locked"])
            self.assertIsNone(player["lockedRank"])

        # Überprüfe, ob die Datei korrekt geschrieben wurde
        mock_open_file.assert_any_call("../data/player_ID.json", "w")
        mock_json_dump.assert_called_once_with(player_data, mock_open_file(), indent=4)

    @patch("builtins.open", new_callable=mock_open, read_data='{"players": [{"playerName": "Player1"}, {"playerName": "Player2"}, {"playerName": "Player3"}]}')
    @patch("json.dump")
    def test_lockLowestPlayer(self, mock_json_dump, mock_open_file):
        # Lade die gemockten Leaderboard-Daten
        with open("../web/data/leaderboard_data.json", "r") as file:
            leaderboard_data = json.load(file)

        # Mock für die Player-Daten mit einem bereits gesperrten Spieler
        with patch("builtins.open", new_callable=mock_open, read_data='{"Player1": {"locked": false}, "Player2": {"locked": true, "lockedRank": 1}, "Player3": {"locked": false}}') as mock_open_player:
            with open("../web/data/player_ID.json", "r") as file:
                player_data = json.load(file)

            # Rufe die Funktion auf
            lockLowestPlayer(player_data, leaderboard_data)

            # Überprüfe, ob der niedrigste ungesperrte Spieler korrekt gesperrt wurde
            self.assertTrue(player_data["Player3"]["locked"])
            self.assertEqual(player_data["Player3"]["lockedRank"], 2)

            # Überprüfe, ob die Datei korrekt geschrieben wurde
            mock_open_player.assert_called_with("../data/player_ID.json", "w")
            mock_json_dump.assert_called_once_with(player_data, mock_open_player(), indent=4)

if __name__ == "__main__":
    unittest.main()