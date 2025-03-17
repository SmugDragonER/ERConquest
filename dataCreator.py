from dotenv import load_dotenv
import requests
from ratelimit import limits, sleep_and_retry
import time
import os
import json

load_dotenv()
API_KEY = os.getenv("API_KEY")

BASE_URL = "https://open-api.bser.io/v1"
seasonID = 29
matchingTeamMode = 3
characterCodeDict = {
    1: "Aya Mini",
    2: "Hyunwoo Mini",
    3: "Jackie Mini",
    4: "Magnus Mini",
    5: "Fiora Mini",
    6: "Nadine Mini",
    7: "Zahir Mini",
    8: "Hart Mini",
    9: "Isol Mini",
    10: "Li Dailin Mini",
    11: "Yuki Mini",
    12: "Hyejin Mini",
    13: "Xiukai Mini",
    14: "Chiara Mini",
    15: "Sissela Mini",
    16: "Silvia Mini",
    17: "Adriana Mini",
    18: "Shoichi Mini",
    19: "Emma Mini",
    20: "Lenox Mini",
    21: "Rozzi Mini",
    22: "Luke Mini",
    23: "Cathy Mini",
    24: "Adela Mini",
    25: "Bernice Mini",
    26: "Barbara Mini",
    27: "Alex Mini",
    28: "Sua Mini",
    29: "Leon Mini",
    30: "Eleven Mini",
    31: "Rio Mini",
    32: "William Mini",
    33: "Nicky Mini",
    34: "Nathapon Mini",
    35: "Jan Mini",
    36: "Eva Mini",
    37: "Daniel Mini",
    38: "Jenny Mini",
    39: "Camilo Mini",
    40: "Chloe Mini",
    41: "Johann Mini",
    42: "Bianca Mini",
    43: "Celine Mini",
    44: "Echion Mini",
    45: "Mai Mini",
    46: "Aiden Mini",
    47: "Laura Mini",
    48: "Tia Mini",
    49: "Felix Mini",
    50: "Elena Mini",
    51: "Priya Mini",
    52: "Adina Mini",
    53: "Markus Mini",
    54: "Karla Mini",
    55: "Estelle Mini",
    56: "Piolo Mini",
    57: "Martina Mini",
    58: "Haze Mini",
    59: "Isaac Mini",
    60: "Tazia Mini",
    61: "Irem Mini",
    62: "Theodore Mini",
    63: "Ly Anh Mini",
    64: "Vanya Mini",
    65: "Debi & Marlene Mini",
    66: "Arda Mini",
    67: "Abigail Mini",
    68: "Alonso Mini",
    69: "Leni Mini",
    70: "Tsubame Mini",
    71: "Kenneth Mini",
    72: "Katja Mini",
    73: "Charlotte Mini",
    74: "Darko Mini",
    75: "Lenore Mini",
    76: "Garnet Mini",
    77: "Yumin Mini",
    78: "Hisui Mini",
    79: "Justyna Mini",
    80: "István Mini",
    81: "NiaH Mini",
    82: "Xuelin Mini"
}

session = requests.Session()
session.headers.update({'x-api-key': API_KEY})

playerIDs = {
    "SmugDragon": {"id": "1927375", "twitch": "SmugDragon"},
    "HajtoNaMotorze": {"id": "1974355", "twitch": "HajtoNaMotorze"},
    "ChocolateDisco": {"id": "1000161", "twitch": "ChocolateDisco"},
    "Strawberryshawty": {"id": "1612676", "twitch": "Strawberryshawty"},
    "Meochi": {"id": "1547682", "twitch": "Meochi"}
}

@sleep_and_retry
@limits(calls=2, period=1)
def rateLimitRequests(url, params = None):
    return session.get(url, params = params)

def getERData(endpoint: str, params: dict = None, retries: int = 5) -> dict:
    url = f"{BASE_URL}/{endpoint}"
    for attempts in range(retries):
        response = rateLimitRequests(url, params)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429:
            time.sleep(2 ** attempts)
        else:
            response.raise_for_status()
    raise Exception("Error")

def getPlayerNum(playerName):
    userInfo = getERData('user/nickname', {'query': playerName})
    userNum = userInfo['user']['userNum']
    playerIDs[playerName] = userNum
    return userNum

def getPlayerData(playerName):
    playerInfo = playerIDs.get(playerName)
    playerNum = playerInfo["id"] if playerInfo else getPlayerNum(playerName)
    twitchLink = playerInfo["twitch"] if playerInfo else ""

    userRawInfo = getERData(f'user/stats/{playerNum}/{seasonID}')
    userInfo = userRawInfo['userStats'][0]
    userMMR = userInfo['mmr']
    userGames = userInfo['totalGames']
    userWR = int((userInfo['totalWins'] / userInfo['totalGames']) * 100) if userGames > 0 else 0
    characterStats = userInfo['characterStats']

    filteredCharacters = []
    for char in characterStats:
        characterCode = char['characterCode']
        characterName = characterCodeDict[characterCode]
        pickRate = round((char['usages'] / userGames) * 100, 1)
        filteredCharacters.append({
            'playerCharacterCode': characterName,
            'playerCharacterPickRate': pickRate
        })

    playerData = {
        "playerName": playerName,
        "playerMMR": userMMR,
        "playerGames": userGames,
        "playerWinRate": userWR,
        "playerCharacterStats": filteredCharacters,
        "playerTwitch": twitchLink
    }
    return playerData


def saveDatatoJson(data,filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def saveAllPlayersToJson(playerDataList, filename):
    sortedPlayerDataList = sorted(playerDataList, key=lambda x: x['playerMMR'], reverse=True)
    data = {"players": sortedPlayerDataList}
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    allPlayersData = []

    for player in playerIDs:
        playerData = getPlayerData(player)
        allPlayersData.append(playerData)
    
    saveAllPlayersToJson(allPlayersData, 'leaderboard_data.json')
