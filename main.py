from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"HNG X task 1, check /api for the task"}


@app.get("/api/")
async def api(slack_name: str, track: str):
    response_data = {
        "slack_name": slack_name,
        "current_day": datetime.now().strftime('%A'),
        "utc_time": datetime.now(pytz.timezone('UTC') ).strftime('%Y-%m-%dT%H:%M:%SZ'),
        "track": track,
        "github_file_url": "https://github.com/Tacticbot/HngTask1/blob/main/main.py",
        "github_repo_url": "https://github.com/Tacticbot/HngTask1",
        "status_code": 200
        }
    return response_data
