from backend.services.leaderboard_creator import get_latest_leaderboard
from backend.utils.util import dict_to_leaderboard, save_data_to_json, leaderboard_to_dict
from backend.services.playerLocker import lockLowestPlayer

from datetime import datetime

'1 load leaderboard'
'2 call the locking function'
'3 save the leaderboard twice (once for normal use, once for logging)'

def main():
    latest_leaderboard_as_dict: dict = get_latest_leaderboard()

    latest_leaderboard = dict_to_leaderboard(latest_leaderboard_as_dict)

    sorted_list = latest_leaderboard.sorted_by_mmr()
    lockLowestPlayer(sorted_list)
    elimination_leaderboard_dict = leaderboard_to_dict(latest_leaderboard)

    timestamp = datetime.now().strftime("%d-%m_%H-%M")
    save_data_to_json(elimination_leaderboard_dict, f'data/leaderboard{timestamp}.json')
    print("Saved normal Json")
    ### For Logging

    timestamp = datetime.now().strftime("%d-%m")
    save_data_to_json(elimination_leaderboard_dict, f'data/Final_Elimination_Results/leaderboard_results_of_{timestamp}.json')
    print("Saved the final result")

if __name__ == "__main__":
    main()