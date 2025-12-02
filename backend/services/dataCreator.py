from dotenv import load_dotenv
import requests
from ratelimit import limits, sleep_and_retry
import time, os, json, datetime, pytz

load_dotenv()
API_KEY = os.getenv("API_KEY")

BASE_URL = "https://open-api.bser.io/v1"
seasonID = 31
matchingTeamMode = 3
characterCodeDict = {
    1: "Jackie Mini", 2: "Aya Mini", 3: "Fiora Mini", 4: "Magnus Mini", 5: "Zahir Mini",
    6: "Nadine Mini", 7: "Hyunwoo Mini", 8: "Hart Mini", 9: "Isol Mini", 10: "Li Dailin Mini",
    11: "Yuki Mini", 12: "Hyejin Mini", 13: "Xiukai Mini", 14: "Chiara Mini", 15: "Sissela Mini",
    16: "Silvia Mini", 17: "Adriana Mini", 18: "Shoichi Mini", 19: "Emma Mini", 20: "Lenox Mini",
    21: "Rozzi Mini", 22: "Luke Mini", 23: "Cathy Mini", 24: "Adela Mini", 25: "Bernice Mini", 
    26: "Barbara Mini", 27: "Alex Mini", 28: "Sua Mini", 29: "Leon Mini", 30: "Eleven Mini",
    31: "Rio Mini", 32: "William Mini", 33: "Nicky Mini", 34: "Nathapon Mini", 35: "Jan Mini",
    36: "Eva Mini", 37: "Daniel Mini", 38: "Jenny Mini", 39: "Camilo Mini", 40: "Chloe Mini",
    41: "Johann Mini", 42: "Bianca Mini", 43: "Celine Mini", 44: "Echion Mini", 45: "Mai Mini",
    46: "Aiden Mini", 47: "Laura Mini", 48: "Tia Mini", 49: "Felix Mini", 50: "Elena Mini",
    51: "Priya Mini", 52: "Adina Mini", 53: "Markus Mini", 54: "Karla Mini", 55: "Estelle Mini",
    56: "Piolo Mini", 57: "Martina Mini", 58: "Haze Mini", 59: "Isaac Mini", 60: "Tazia Mini",
    61: "Irem Mini", 62: "Theodore Mini", 63: "Ly Anh Mini", 64: "Vanya Mini", 65: "Debi & Marlene Mini",
    66: "Arda Mini", 67: "Abigail Mini", 68: "Alonso Mini", 69: "Leni Mini", 70: "Tsubame Mini",
    71: "Kenneth Mini", 72: "Katja Mini", 73: "Charlotte Mini", 74: "Darko Mini", 75: "Lenore Mini",
    76: "Garnet Mini", 77: "Yumin Mini", 78: "Hisui Mini", 79: "Justyna Mini", 80: "István Mini",
    81: "NiaH Mini", 82: "Xuelin Mini"
}

session = requests.Session()
session.headers.update({'x-api-key': API_KEY})

with open("../web/data/player_ID.json", "r", encoding="utf-8") as file:
    playerIDs = json.load(file)

lockedPlayers=[]
unlockedPlayers=[]
currentlyLockedPlayers = 0

@sleep_and_retry
@limits(calls=2, period=1)
def rateLimitRequests(url, params = None):
    return session.get(url, params = params)

def buildAllPlayerData(playerIDs):
    all_players = []
    for player in playerIDs.keys():
        try:
            print(f"updating {player} at the moment")
            player_data = getPlayerData(player)
            all_players.append(player_data)
        except Exception as e:
            print(f"Error with player {player}")
            # fill everything with 0
            player_info = playerIDs.get(player)
            twitch_link = player_info["twitch"]
            player_data = {
                "playerName": player,
                "playerMMR": 0,
                "playerGames": 0,
                "playerWinRate": 0,
                "playerCharacterStats": None,
                "playerTwitch": twitch_link
                }
            all_players.append(player_data)
    return all_players

def sortPlayers(player_IDs,all_player_data) -> list[dict, dict]:
# send in all player data
# sort the it based on eliminated and alive players
# return the sorted list

    locked = [] #Eliminated for Order
    unlocked = [] #Still alive

    for player in all_player_data: 
        if not player_IDs.get(player["playerName"], {}).get("locked", False): # Nicht Eliminiert
            unlocked.append(player)
        else:
            locked.append(player)


    unlocked.sort(key=lambda x: x["playerMMR"], reverse=True) # Sort based on MMR
    locked.sort(key=lambda x: player_IDs.get(x["playerName"], {}).get("lockedRank", float('inf'))) # Sort based on lockedRank
    
    return unlocked + locked

def saveAllPlayersToJson(playerDataList, filename):

    data = {"players": playerDataList}
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def saveCurrentTime() -> None :
    cet_timezone = pytz.timezone("Europe/Paris")
    currentTime = datetime.datetime.now(cet_timezone)

    if currentTime.minute >= 15 and currentTime.minute < 44:
        roundedTime = currentTime.replace(minute=30, second=0, microsecond=0)

    elif currentTime.minute >= 45:
        currentTime = currentTime + datetime.timedelta(hours=1)
        roundedTime = currentTime.replace(minute=0, second=0, microsecond=0)

    else: #currentTime.minute < 15:
        roundedTime = currentTime.replace(minute=0, second=0, microsecond=0)

    formattedTime = roundedTime.strftime("Last Update: %d.%m at %H:%M CEST")
    print(formattedTime)
    with open("../web/data/last_updated.json", 'w') as json_file:
        json.dump(formattedTime,json_file, indent=4)
    print("Current Time Saved")
