import json
from .erAPI import get_player_id, get_player_stats
import time
### Fetch Data

def get_all_player_ids(player_name_list) -> dict:
    player_id_dict = {}
    for pn in player_name_list:
        current_player_id: int = get_player_id(pn)
        player_id_dict[pn] = current_player_id
    return player_id_dict

def get_all_player_stats(player_name_list: list, player_id_dict: dict) -> dict:
    all_player_stats_dict = {}
    for pn in player_name_list:
        current_player_id: int = player_id_dict[pn]
        all_player_stats_dict[pn] = get_player_stats(current_player_id)
        time.sleep(1)
    return all_player_stats_dict 

def get_data_from_json(filename):
    with open("../data/{filename}", 'r', encoding="utf-8") as file:
        data = json.load(file)
        return data

# conquest_data.json
# {
#     "players": [
#         {
#            "playerName": "FDGood",
#             "playerMMR": 7672,
#             "playerGames": 172,
#             "playerWinRate": 15,
#             "playerCharacterStats": [
#                 {
#                     "playerCharacterCode": "Li Dailin Mini",
#                     "playerCharacterPickRate": 48.3
#                 },
#                 {
#                     "playerCharacterCode": "Istv\u00e1n Mini",
#                     "playerCharacterPickRate": 30.2
#                 },
#                 {
#                     "playerCharacterCode": "Piolo Mini",
#                     "playerCharacterPickRate": 12.2
#                 }
#             ],
#             "playerTwitch": "FDGoodVX",
#             "isLiveOnTwitch": bool,
#             "isLocked": bool,
#             "lockedRank": int,
#         }



### FOR LATER USE
# def build_tournament_data(playerIDs):
    # all_players = []
    # for player in playerIDs.keys():
    #     try:
    #         print(f"updating {player} at the moment")
    #         player_data = getPlayerData(player)
    #         all_players.append(player_data)
    #     except Exception as e:
    #         print(f"Error with player {player}")
    #         # fill everything with 0
    #         player_info = playerIDs.get(player)
    #         twitch_link = player_info["twitch"]
    #         player_data = {
    #             "playerName": player,
    #             "playerMMR": 0,
    #             "playerGames": 0,
    #             "playerWinRate": 0,
    #             "playerCharacterStats": None,
    #             "playerTwitch": twitch_link
    #             }
    #         all_players.append(player_data)
    # return all_players

# def sortPlayers(player_IDs,all_player_data) -> list[dict, dict]:
# #TODO: player_IDs shouldn't be needed
# # send in all player data
# # sort the it based on eliminated and alive players
# # return the sorted list

#     locked = [] #Eliminated for Order
#     unlocked = [] #Still alive

#     for player in all_player_data: 
#         if not player_IDs.get(player["playerName"], {}).get("locked", False): # Nicht Eliminiert
#             unlocked.append(player)
#         else:
#             locked.append(player)


#     unlocked.sort(key=lambda x: x["playerMMR"], reverse=True) # Sort based on MMR
#     locked.sort(key=lambda x: player_IDs.get(x["playerName"], {}).get("lockedRank", float('inf'))) # Sort based on lockedRank
    
#     return unlocked + locked
