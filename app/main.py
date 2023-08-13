from fastapi import FastAPI

from app.src.worker.prefect_task import repo_info

app = FastAPI()


@app.put("/temperature")
def get_temperature():
    return {"Message": "200 OK"}

@app.get("/start")
def start_flow():
    repo_info_val, contributors = repo_info()
    return {"Name:": repo_info_val, "Contributors:": contributors}
