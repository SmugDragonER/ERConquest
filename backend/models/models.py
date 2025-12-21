from dataclasses import dataclass, field
from typing import Dict, List, Optional

@dataclass
class PlayerSignUpData:
    Name: str
    Twitch: str
    Discord: str
    IMG: str

@dataclass
class PlayerLeaderboardEntry:
    name: str
    mmr: int
    games: int
    wins: int
    win_rate: float
    character_stats: List[Dict[str,any]]
    twitch: str
    is_live_on_twitch: bool
    is_eliminated: bool
    eliminated_at_rank: Optional[int]

@dataclass
class Leaderboard:
    entries: dict[str, PlayerLeaderboardEntry] = field(default_factory=dict) #bei jedem neuen Leaderboard ein frisches leeres dict erstellen

    def add_entry(self, entry: PlayerLeaderboardEntry) -> None:
        self.entries[entry.name] = entry
    
    def get(self, name:str) -> Optional[PlayerLeaderboardEntry]:
        return self.entries.get(name)
    
    def sorted_by_mmr(self) -> list[PlayerLeaderboardEntry]:
        return sorted(self.entries.values(), key = lambda e: e.mmr, reverse=True)

