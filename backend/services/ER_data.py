import json
from .erAPI import get_player_id, get_player_stats
import time
from pathlib import Path

### Static
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR.parent / "data"

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

def get_data_from_json(filename: str):
    '''
    Returns the data as a dict
    '''
    path = DATA_DIR / filename
    with path.open('r', encoding="utf-8") as file:
        data = json.load(file)
        return data
