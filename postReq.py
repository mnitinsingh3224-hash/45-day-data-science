from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name : str
    age : int

@app.post("/student")
def get_student(student : Student):
    return {
        "message" : "Student created successfully",
        "student" : student
    }