from backend.models.models import PlayerLeaderboardEntry

def unlockAllPlayer(sorted_leaderboard: list[PlayerLeaderboardEntry]):
    for player in sorted_leaderboard:
        player.is_eliminated = False
        player.eliminated_at_rank = None
    return sorted_leaderboard

def lockLowestPlayer(sorted_leaderboard: list[PlayerLeaderboardEntry]):
    '''  
    Locks the lowest player and saves their placement
    '''

    if isinstance(sorted_leaderboard, list):
        for original_index, player in reversed(list(enumerate(sorted_leaderboard))):
            if not player.is_eliminated:
                player.is_eliminated = True
                player.eliminated_at_rank = original_index
                break
    return sorted_leaderboard
