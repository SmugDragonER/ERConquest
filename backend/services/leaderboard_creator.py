from typing import Dict
import time
from pathlib import Path
from ..models.models import PlayerLeaderboardEntry, Leaderboard
from .twitchAPI import check_is_player_live
from .loadSignupDataFromCsv import load_signups_from_csv
from .ER_data import get_all_player_ids, get_all_player_stats, get_data_from_json
from .constants import characterCodeDict

def get_top_character_icons(character_stats, top_n=3):
    if not character_stats:
        return []

    top = sorted(character_stats, key=lambda cs: cs.get("totalGames", 0), reverse=True)[:top_n]

    icons = []
    for cs in top:
        code = cs.get("characterCode")
        base_name = characterCodeDict.get(code)
        if base_name:
            icons.append(f"{base_name}.png") 
    return icons

def create_leaderboard_data( player_id_dict: Dict[str, int], all_player_stats_dict: Dict[str, dict], signups_by_name: Dict[str, PlayerLeaderboardEntry]) -> Leaderboard:
    lb = Leaderboard()

    # create a new leaderboard and fill it with given data

    for pn in player_id_dict:

        user_stats_json = all_player_stats_dict[pn] #player_name : dict (the json)
        user_stats_list = user_stats_json["userStats"] #from the json the userStats list
        user_stats_entry = user_stats_list[0] # there is only 1 element in the list
        
        mmr = user_stats_entry["mmr"] #in the userStats list, get the value of the mmr key
        games = user_stats_entry["totalGames"]
        wins = user_stats_entry["totalWins"]
        win_rate = round((wins/games)*100,1) if games > 0 else 0

        character_stats = user_stats_entry["characterStats"]
        top_character_icons = get_top_character_icons(character_stats, 3)
        player_twitch = signups_by_name[pn].Twitch
        is_live_on_twitch: bool = check_is_player_live(player_twitch)
        is_eliminated: bool = False
        eliminated_at_rank = None

        lb.add_entry(
            PlayerLeaderboardEntry(
                name=pn,
                mmr=mmr,
                games=games,
                wins=wins,
                win_rate=win_rate,
                character_stats=character_stats,
                top_character_icons=top_character_icons,
                twitch= player_twitch,
                is_live_on_twitch=is_live_on_twitch,
                is_eliminated=is_eliminated,
                eliminated_at_rank=None,
            )
        )
    return lb

def build_leaderboard():

    #fetches the data, creates the leaderboard and fills it; sorted by mmr

    signups_list = load_signups_from_csv("data/EU_Conquest_2_Season_10_signup_data.csv")
    signups_by_name = {s.Name: s for s in signups_list}

    player_id_dict = get_all_player_ids(signups_by_name.keys()) # Dict - Key: PlayerName, Value: Player ID
    all_player_stats_dict = get_all_player_stats(signups_by_name,player_id_dict)    # Dict - Key: PlayerName, Value: PlayerStats

    lb = create_leaderboard_data(player_id_dict, all_player_stats_dict, signups_by_name)

    return lb

def get_latest_leaderboard():
    
    # gets the latest saved leaderboard from the data folder

    DATA_PATH = Path(__file__).resolve().parents[2]/"data"
    files = [p for p in DATA_PATH.glob("leaderboard*.json") if p.is_file()]
    if not files:
        return None
    latest = max(files, key=lambda p: p.stat().st_mtime)
    lb = get_data_from_json(latest.name)
    return lb