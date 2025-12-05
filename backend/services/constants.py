from dotenv import load_dotenv
import os
from enum import Enum

### CONSTANT DATA ###
# This shouldn't never change, only updated if ER Api gets updated
seasonID = 31

class MatchingMode(Enum):
    NORMAL = 2
    RANKED = 3

class MatchingTeamMode(Enum):
    SOLO = 1
    DUO = 2
    SQUAD = 3

player_name_list = ["SmugDragon", "Patreii"]

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
load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://open-api.bser.io/"
