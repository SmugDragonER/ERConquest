import json
from datetime import datetime
from fastapi import FastAPI
import uvicorn
from backend.services.ER_data import get_all_player_ids, get_all_player_stats
from backend.services.constants import player_name_list
from backend.scripts.setup_data import setup
from backend.services.leaderboard_creator import build_leaderboard
from backend.utils.util import leaderboard_to_dict, save_data_to_json

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/update_all_player_data")
async def update_all_player_data():
    return get_all_player_stats(player_name_list=player_name_list)

@app.get("/update_all_player_ids")
async def update_all_player_ids():
    return get_all_player_ids(player_name_list) 

@app.get("/build_leaderboard")
async def send_leaderboard():
    lb = build_leaderboard()
    lb_json = leaderboard_to_dict(lb)
    timestamp = datetime.now().strftime("%d-%m_%H-%M")
    save_data_to_json(lb_json, f'leaderboard{timestamp}.json')
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