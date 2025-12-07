from typing import Dict

from ..models.models import PlayerLeaderboardEntry, Leaderboard
from .twitchAPI import check_is_player_live
from .loadSignupDataFromCsv import load_signups_from_csv
from .ER_data import get_all_player_ids, get_all_player_stats

def create_leaderboard_data(
        player_id_dict: Dict[str, int],
        all_player_stats_dict: Dict[str, dict],
        signups_by_name: Dict[str, PlayerLeaderboardEntry],
        ) -> Leaderboard:
    lb = Leaderboard()


    for pn in player_id_dict:

        user_stats_json = all_player_stats_dict[pn] #player_name : dict (the json)
        user_stats_list = user_stats_json["userStats"] #from the json the userStats list
        user_stats_entry = user_stats_list[0] # there is only 1 element in the list
        
        mmr = user_stats_entry["mmr"] #in the userStats list, get the value of the mmr key
        games = user_stats_entry["totalGames"]
        wins = user_stats_entry["totalWins"]
        win_rate = wins/games if games > 0 else 0

        character_stats = user_stats_entry["characterStats"]
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
                twitch= player_twitch,
                is_live_on_twitch=is_live_on_twitch,
                is_eliminated=is_eliminated,
                eliminated_at_rank=None,
            )
        )
    return lb

def build_leaderboard():
    signups_list = load_signups_from_csv("...")
    signups_by_name = {s.Name: s for s in signups_list}

    player_id_dict = get_player_id_dict(signups_by_name.key())
    all_player_stats_dict = get_all_player_stats(player_id_dict)
    lb = create_leaderboard_data(player_id_dict, all_player_stats_dict, signups_by_name)
    return lb