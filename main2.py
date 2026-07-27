from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome"}


@app.get("/student/{roll}")
def student(roll: int):
    return {
        "roll": roll,
        "name": "Deepak"
    }


@app.get("/search")
def search(item: str):
    return {
        "search": item
    }