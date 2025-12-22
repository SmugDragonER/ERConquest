from dataclasses import asdict
from backend.models.models import Leaderboard, PlayerLeaderboardEntry
import json
from pathlib import Path

def leaderboard_to_dict(lb: Leaderboard) -> dict:
    return {
        "entries": {
            name: asdict(entry)
            for name, entry in lb.entries.items()
        }
    }

def dict_to_leaderboard(data: dict) -> Leaderboard:
    leaderboard = Leaderboard()
    for name, entry_dict in data["entries"].items():
        leaderboard.add_entry(PlayerLeaderboardEntry(**entry_dict))
    return leaderboard

def save_data_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
