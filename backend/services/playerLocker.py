from backend.models.models import PlayerLeaderboardEntry, Leaderboard

def unlockAllPlayer(sorted_leaderboard: list[PlayerLeaderboardEntry]):
    for player in sorted_leaderboard:
        player.is_eliminated = False
        player.eliminated_at_rank = None
    return sorted_leaderboard

def lockLowestPlayer(lb: Leaderboard):
    '''  
    Locks the lowest player and saves their placement
    '''

    sorted_player_list = lb.sorted_by_mmr()

    for original_index, player in reversed(list(enumerate(sorted_player_list))):
        if not player.is_eliminated:
            player.is_eliminated = True
            player.eliminated_at_rank = original_index +1
            break
    return lb
