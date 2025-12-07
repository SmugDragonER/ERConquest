from ..services.loadSignupDataFromCsv import load_signups_from_csv



def test_load_signups_from_csv():
    signups = load_signups_from_csv("data/test_signup_data.csv")
    assert len(signups) == 2

    first = signups[0]
    assert first.Name == "SmugDragon"
    assert first.Twitch == "smugdragon"
    assert first.IMG == "SmugDragon.png"


    

