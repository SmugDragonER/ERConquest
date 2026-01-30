import requests
from .constants import CLIENT_ID, CLIENT_SECRET, GRANT_TYPE,TWITCH_SEARCH_CHANNEL_URL
import time

access_token:str | None = None
_token_expiry = 0

def get_app_access_token() -> str:
    # gets the twitch access token if old one is expired

    global access_token, _token_expiry

    now = time.time()

    if access_token is not None and now < _token_expiry - 30:
        return access_token 

    body_data = {"client_id": CLIENT_ID, "client_secret": CLIENT_SECRET, "grant_type": GRANT_TYPE}
    client_credentials_response = requests.post("https://id.twitch.tv/oauth2/token", data=body_data)
    client_credentials_response.raise_for_status() #Error
    token_json = client_credentials_response.json()
    access_token = token_json["access_token"]
    _token_expiry = now + token_json["expires_in"]
    return access_token



def check_is_player_live(player_twitch: str) -> bool:
    try:
        token = get_app_access_token()
        
        headers = {
            "Client-ID": CLIENT_ID,
            "Authorization": f"Bearer {token}",
        }
        url = f"https://api.twitch.tv/helix/streams?user_login={player_twitch.lower()}"
        

        r = requests.get(url, headers=headers)
        r.raise_for_status()
        search_channel_json = r.json()
        data = r.json().get("data", [])
        return len(data) > 0
    except Exception as e:
        print(f"Twitch check failed for {player_twitch}: {e}")
        return False
