from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class StudentResponse(BaseModel):
    name : str


class Student(BaseModel):
    name : str
    password : int


@app.post("/student" , response_model = StudentResponse)
def create_student(student : Student):
    return student