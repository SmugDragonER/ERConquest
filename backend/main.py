from datetime import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from backend.services.ER_data import get_all_player_ids, get_all_player_stats
from backend.services.constants import player_name_list
from backend.services.leaderboard_creator import build_leaderboard, get_latest_leaderboard
from backend.utils.util import leaderboard_to_dict, save_data_to_json

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

@app.get("/update_all_player_data")
async def update_all_player_data():
    return get_all_player_stats(player_name_list=player_name_list)

@app.get("/update_all_player_ids")
async def update_all_player_ids():
    return get_all_player_ids(player_name_list) 

@app.get("/get_latest_leaderboard")
async def get_leaderboard_data():
    lb = get_latest_leaderboard()
    if lb is None:
        raise HTTPException(status_code=404, detail="No leaderboard found")
    return lb


@app.get("/build_leaderboard")
async def send_leaderboard():
    """
    Does: Builds a python object, turns it into a dict + save with current time 
    Returns: leaderboard dict
    """
    lb = build_leaderboard()
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