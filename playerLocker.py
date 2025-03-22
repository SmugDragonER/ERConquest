import json

# Load player data
with open("player_ID.json", "r") as file:
    player_data = json.load(file)

# Load leaderboard data
with open("leaderboard_data.json", "r") as file:
    leaderboard_data = json.load(file)

def unlockAllPlayer(player_data):
    for player in player_data.values():
        player["locked"] = False
        player["lockedRank"] = None
    with open ("player_ID.json", "w") as file:
        json.dump(player_data, file , indent=4)

def lockLowestPlayer(player_data, leaderboard_data):
    players = leaderboard_data.get("players", [])
    
    if isinstance(players, list) and players:
        for index, player in enumerate(reversed(players)):
            player_name = player["playerName"]
            if not player_data.get(player_name, {}).get("locked", False):
                player_data[player_name]["locked"] = True
                locked_rank = len(players) - 1 - index
                player_data[player_name]["lockedRank"] = locked_rank
                with open("player_ID.json", "w") as file:
                    json.dump(player_data, file, indent=4)
                break

if __name__ == "__main__":

  lockLowestPlayer(player_data, leaderboard_data)