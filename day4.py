from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int


@app.post("/student")
def create_student(student: Student):
    return {
        "message": "Student Created",
        "student": student
    }


@app.put("/student/{id}")
def update_student(id: int, student: Student):
    return {
        "message": "Student Updated",
        "id": id,
        "student": student
    }


@app.delete("/student/{id}")
def delete_student(id: int):
    return {
        "message": "Student Deleted",
        "id": id
    }