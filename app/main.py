import datetime

from fastapi import FastAPI

from app.src.flows.get_github import repo_info
from app.src.flows.save_temperature import save_temperature

app = FastAPI()


@app.get("/start")
def start_flow():
    repo_info_val, contributors = repo_info()
    return {"Name:": repo_info_val, "Contributors:": contributors}


@app.post("/send_temperature")
async def send_temperature(date: datetime.date, temperature: float):
    save_temperature(date, temperature)
    return {"message": "Temperature sent!"}