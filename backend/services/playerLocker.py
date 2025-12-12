import json
from backend.models.models import Leaderboard

# Load player data
with open("../web/data/player_ID.json", "r") as file:
    player_data = json.load(file)

# Load leaderboard data
with open("../web/data/leaderboard_data.json", "r") as file:
    leaderboard_data = json.load(file)

def unlockAllPlayer(player_data):
    for player in player_data.values():
        player["locked"] = False
        player["lockedRank"] = None
    return player_data

def lockLowestPlayer(Leaderboard):
    sorted_lb = Leaderboard.sorted_by_mmr()
    players_dict = sorted_lb.entries
    
    for index, players in enumerate(reversed(players)):
        player_name = players.name


    
    if isinstance(players, list) and players:
        for index, player in enumerate(reversed(players)):
            player_name = player["playerName"]
            if not player_data.get(player_name, {}).get("locked", False):
                player_data[player_name]["locked"] = True
                locked_rank = len(players) - 1 - index
                player_data[player_name]["lockedRank"] = locked_rank
                break
    return player_data
