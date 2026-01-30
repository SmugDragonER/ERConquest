from datetime import datetime
from fastapi import FastAPI, HTTPException, APIRouter, Query
from fastapi.middleware.cors import CORSMiddleware
import uvicorn, os
from backend.services.leaderboard_creator import build_leaderboard, get_latest_leaderboard
from backend.utils.util import leaderboard_to_dict, dict_to_leaderboard, save_data_to_json
from dotenv import load_dotenv

load_dotenv()
ADMIN_SECRET_KEY = os.getenv("ADMIN_SECRET_KEY")
app = FastAPI()

router = APIRouter(prefix="/api")

#app.router.prefix = "/api"
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://smugdragon.xyz",
    "https://www.smugdragon.xyz",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
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

@router.get("/get_latest_leaderboard")
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

@router.get("/build_leaderboard")
async def send_leaderboard(key: str = Query(None)):
    """
    Fully fetches new data, creates a new leaderboard and saves it with the current time at the end
    """
    if key != ADMIN_SECRET_KEY:
        raise HTTPException(status_code=401, detail="You cant do that buddy")
    lb = build_leaderboard() # sorted by mmr

    lb_json = leaderboard_to_dict(lb)

    timestamp = datetime.now().strftime("%d-%m_%H-%M")
    save_data_to_json(lb_json, f'data/leaderboard{timestamp}.json')
    return lb_json


app.include_router(router)

def main():
    uvicorn.run(
        "main:app",   # falls die Datei main.py heißt
        host="127.0.0.1",
        port=8000,
        reload=False,
    )

if __name__ == "__main__":
    main()