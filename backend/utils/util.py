from dataclasses import asdict
from ..models.models import Leaderboard, PlayerLeaderboardEntry

def leaderboard_to_dict(lb: Leaderboard) -> dict:
    return {
        "entries": {
            name: asdict(PlayerLeaderboardEntry)
            for name, PlayerLeaderboardEntry in lb.entries.items()
        }
    }

