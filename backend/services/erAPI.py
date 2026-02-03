import json
import requests
import time
from ratelimit import limits, sleep_and_retry
from .constants import MatchingMode, seasonID, ER_BASE_URL, API_KEY
# Create a session to persist certain parameters across requests
session = requests.Session()
session.headers.update({'x-api-key': API_KEY})

# Rate limit: 1 request per second, 2 requests in a burst
@sleep_and_retry
@limits(calls=1, period=2)
def rate_limited_request(url, params=None):
    # Make a rate-limited request
    return session.get(url, params=params)

### API REQUESTS ###
#This has to be limited as much as possible due to the rate limit
#of 1 request per second

def get_ER_data(endpoint: str, params: dict = None) -> dict:
    # Construct the full URL
    url = f"{ER_BASE_URL}{endpoint}"
    response = rate_limited_request(url, params)
    if response.status_code == 200:
        # Return the JSON response if successful
        return response.json()
    else:
        # Raise an error for other status codes
        print(f"Error: {response.status_code} - {response.text}")
        response.raise_for_status()

def get_player_id(player_name:str) -> int:


    fixed_name = player_name
    if "Arky" in player_name:
        fixed_name = player_name.replace("--", "").strip()

    # Get the user number for a given player name
    user_info = get_ER_data('v1/user/nickname', {'query': fixed_name})
    if not user_info or 'user' not in user_info:
        print(f"CRITICAL: Player '{player_name}' not found or API error! Response: {user_info}")
        return 0
    player_id: int = user_info['user']['userId']
    return player_id

### FILTER DICT ###
#Filtering through the response
#Used to ask the API directly but changed due to rate limit

def get_player_stats(player_id: int, season_id: int = seasonID, matching_mode: int = MatchingMode.RANKED) -> dict:
    player_stats = get_ER_data(f'v2/user/stats/uid/{player_id}/{season_id}/{matching_mode.value}')
    return player_stats

def get_user_rank(user_info) -> int:
    user_mmr = user_info['userRank']['mmr']
    return user_mmr