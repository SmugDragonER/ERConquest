from ..models.models import PlayerSignUpData
from typing import List
import csv

def load_signups_from_csv(path: str) -> List[PlayerSignUpData]:
    signups: List[PlayerSignUpData] = []
    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file) # Uses Header as Keys
        for row in reader:

            ### fix twitch user input
            Twitch_input = row["Twitch"].lower()
            if "twitch.tv" in Twitch_input:
                Twitch_string = Twitch_input.split("/")
                Twitch = Twitch_string[-1]
            else: Twitch=Twitch_input
            

            
            signups.append(
                PlayerSignUpData(
                    Name = row["In-Game-Name"],
                    Twitch = Twitch,
                    Discord = row["Discord-Name"],
                    IMG= f"{row["In-Game-Name"]}.png",
                )
            )
    
    return signups