import json
from fastapi import FastAPI
from services.ER_data import get_all_player_ids, get_all_player_stats
from services.constants import player_name_list
from scripts.setup_data import setup

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

@app.post("/admin/setup")
def run_setup():
    setup(player_name_list)
    return{"status": "ok"}
