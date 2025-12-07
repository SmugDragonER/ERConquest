from ..services.leaderboard_creator import create_leaderboard_data
from ..models.models import PlayerSignUpData
from backend.services import leaderboard_creator

## MOCK DATA ##

all_player_stats_dict = {
    "SmugDragon": {
        "code": 200,
        "message": "Success",
        "userStats": [
            {
                "seasonId": 33,
                "matchingMode": 3,
                "matchingTeamMode": 3,
                "mmr": 3107,
                "nickname": "SmugDragon",
                "rank": 10,
                "rankSize": 50,
                "totalGames": 5,
                "totalWins": 2,
                "totalTeamKills": 70,
                "totalDeaths": 8,
                "escapeCount": 0,
                "rankPercent": 0.2,
                "averageRank": 2.4,
                "averageKills": 14.0,
                "averageAssistants": 1.0,
                "averageHunts": 30.0,
                "top1": 0.4,
                "top2": 0.6,
                "top3": 0.8,
                "top5": 1.0,
                "top7": 1.0,
                "characterStats": [
                    {
                        "characterCode": 78,
                        "totalGames": 3,
                        "usages": 3,
                        "maxKillings": 18,
                        "top3": 2,
                        "wins": 1,
                        "top3Rate": 0.67,
                        "averageRank": 2
                    },
                    {
                        "characterCode": 23,
                        "totalGames": 2,
                        "usages": 2,
                        "maxKillings": 10,
                        "top3": 1,
                        "wins": 1,
                        "top3Rate": 0.5,
                        "averageRank": 3
                    }
                ]
            }
        ]
    },
    "Leitnessen": {
        "code": 200,
        "message": "Success",
        "userStats": [
            {
                "seasonId": 33,
                "matchingMode": 3,
                "matchingTeamMode": 3,
                "mmr": 2950,
                "nickname": "Leitnessen",
                "rank": 20,
                "rankSize": 50,
                "totalGames": 4,
                "totalWins": 1,
                "totalTeamKills": 40,
                "totalDeaths": 6,
                "escapeCount": 0,
                "rankPercent": 0.4,
                "averageRank": 3.0,
                "averageKills": 10.0,
                "averageAssistants": 0.5,
                "averageHunts": 25.0,
                "top1": 0.25,
                "top2": 0.5,
                "top3": 0.5,
                "top5": 0.75,
                "top7": 1.0,
                "characterStats": [
                    {
                        "characterCode": 43,
                        "totalGames": 2,
                        "usages": 2,
                        "maxKillings": 8,
                        "top3": 1,
                        "wins": 1,
                        "top3Rate": 0.5,
                        "averageRank": 3
                    },
                    {
                        "characterCode": 23,
                        "totalGames": 2,
                        "usages": 2,
                        "maxKillings": 6,
                        "top3": 0,
                        "wins": 0,
                        "top3Rate": 0.0,
                        "averageRank": 4
                    }
                ]
            }
        ]
    }
}

player_id_dict = {
    "SmugDragon": 101,
    "Leitnessen": 102,
}

# MOCK SIGNUPS
signups_by_name = {
    "SmugDragon": PlayerSignUpData(
        Name="SmugDragon",
        Twitch="smugdragon",
        Discord="smugdragoner",
        IMG="SmugDragon.png",
    ),
    "Leitnessen": PlayerSignUpData(
        Name="Leitnessen",
        Twitch="leitnessen",
        Discord="Leitnessen",
        IMG="Leit.png",
    ),
}


def test_create_leaderboard_data(monkeypatch):

    def fake_check_is_player_live(_):
        return False
    monkeypatch.setattr(leaderboard_creator, "check_is_player_live", fake_check_is_player_live)
    
    lb = create_leaderboard_data(player_id_dict, all_player_stats_dict,signups_by_name)

    assert len(lb.entries) == 2

    SmugDragon = lb.entries["SmugDragon"]
    assert SmugDragon.mmr == 3107
    assert SmugDragon.games == 5
    assert SmugDragon.wins == 2

    Leit = lb.entries["Leitnessen"]
    assert Leit.mmr == 2950
    assert Leit.games == 4
    assert Leit.wins == 1