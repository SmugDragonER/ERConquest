from dataclasses import asdict
from backend.models.models import Leaderboard, PlayerLeaderboardEntry
import json
from pathlib import Path

def leaderboard_to_dict(lb: Leaderboard) -> dict:
    return {
        "entries": {
            name: asdict(PlayerLeaderboardEntry)
            for name, PlayerLeaderboardEntry in lb.entries.items()
        }
    }


def save_data_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

