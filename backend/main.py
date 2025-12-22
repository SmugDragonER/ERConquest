from datetime import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from backend.services.constants import player_name_list, characterCodeDict
from backend.services.leaderboard_creator import build_leaderboard, get_latest_leaderboard
from backend.utils.util import leaderboard_to_dict, dict_to_leaderboard, save_data_to_json

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    return {"message": "Hello World"}

## NOT NEEDED ANYMORE
# @app.get("/update_all_player_data")
# async def update_all_player_data():
#     return get_all_player_stats(player_name_list=player_name_list)

## NOT NEEDED ANYMORE
# @app.get("/update_all_player_ids")
# async def update_all_player_ids():
    # return get_all_player_ids(player_name_list) 

@app.get("/get_latest_leaderboard")
async def get_leaderboard_data():
    lb_data = get_latest_leaderboard()
    if lb_data is None:
        raise HTTPException(status_code=404, detail="No leaderboard found")

    # If get_latest_leaderboard returns dict from JSON, convert it
    if isinstance(lb_data, dict):
        lb = dict_to_leaderboard(lb_data)
    else:
        lb = lb_data

    return leaderboard_to_dict(lb)

@app.get("/build_leaderboard")
async def send_leaderboard():
    """
    Fully fetches new data, creates a new leaderboard and saves it with the current time at the end
    """
    lb = build_leaderboard() # sorted by mmr

    lb_json = leaderboard_to_dict(lb)

    timestamp = datetime.now().strftime("%d-%m_%H-%M")
    save_data_to_json(lb_json, f'data/leaderboard{timestamp}.json')
    return lb_json

def main():
    uvicorn.run(
        "main:app",   # falls die Datei main.py heißt
        host="127.0.0.1",
        port=8000,
        reload=True,
    )

if __name__ == "__main__":
    main()