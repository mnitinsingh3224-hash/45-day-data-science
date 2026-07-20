from fastapi import FastAPI 

app = FastAPI()

@app.get("/product/{id}")
def get_product(id):
    return {"message" : id}

@app.get("/student/{rollNO}")
def student(rollNO):
    return {"rollNo" : rollNO}

# Query parameter :
@app.get("/search")
def search(item : str):
    return {"searching": item}