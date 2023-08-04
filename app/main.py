from fastapi import FastAPI

app = FastAPI()


@app.put("/temperature")
def get_temperature():
    return {"Message": "200 OK"}
