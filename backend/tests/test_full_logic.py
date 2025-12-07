import pytest
from ..services.loadSignupDataFromCsv import load_signups_from_csv
from ..services.ER_data import get_all_player_ids, get_all_player_stats
from ..services.leaderboard_creator import build_leaderboard, create_leaderboard_data

# this test is just here to see if the backend runs through without errors
@pytest.mark.integration
def test_full_logic():
    lb = build_leaderboard()
    

    assert len(lb.entries) > 0