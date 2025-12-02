
import json
from backend.services import ER_data, playerLocker

def main ():
    ### LOAD DATA ###
    with open("../data/player_ID.json", "r", encoding="utf-8") as file:
        playerIDs = json.load(file)

    with open("../data/leaderboard", "r", encoding="utf-8") as file:
        playerIDs = json.load(file)


    ER_data.buildAllPlayerData()
    ER_data.sortPlayers()
    playerLocker.lockLowestPlayer()
    playerLocker.unlockAllPlayer()



    ###TODO: FastAPI
    ### 1. Grundgerüst
    #2. bestehende einbinden
    #3. vue