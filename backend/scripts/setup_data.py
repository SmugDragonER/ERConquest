from backend.utils.util import save_data_to_json
from backend.services.ER_data import (
    get_all_player_ids,
    get_all_player_stats,
)


def setup(player_name_list):
    player_ids = get_all_player_ids(player_name_list)
    save_data_to_json(player_ids, "player_name_to_id.json")
    player_stats = get_all_player_stats(player_name_list, player_ids)
    save_data_to_json(player_stats, "player_stats.json")
    print("setup done!")


if __name__ == "__main__":
    playerList = [
        "KitasanBlack", "Arkyー", "Leitnessen", "MajinTenshinhan", 
        "Gtracks", "Baumi", "HajtoNaMotorze", "ImNotBreathing", 
        "yaebalturel", "Kudeta", "Yazidron", "LewMalpa", 
        "Yoruchan", "DEADDEADDEMONS", "Lesys", "Denzy", 
        "Photograph", "GonnaEinALittle", "FDGood", "Nyabi", 
        "SmugDragon"
    ]
    
    print(f"Starting setup for {len(playerList)} players...")
    setup(playerList)