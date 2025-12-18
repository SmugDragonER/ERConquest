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
    # check if given player is live on twitch

    # token = get_app_access_token()
    # params = {
    #     "query": player_twitch,
    # }

    # headers = {
    #     "Client-ID": CLIENT_ID,
    #     "Authorization": f"Bearer {token}",
    # }

    # r = requests.get(TWITCH_SEARCH_CHANNEL_URL, headers=headers, params=params)
    # r.raise_for_status()
    # search_channel_json = r.json()
    # data = search_channel_json.get("data", [])
    # if not data:
    #     raise ValueError(f"No Twitch channel found for: {player_twitch}, check for spelling mistake or account deletion")
    
    # first_entry = data[0]
    # is_player_live = first_entry["is_live"]
    is_player_live = False
    return is_player_live