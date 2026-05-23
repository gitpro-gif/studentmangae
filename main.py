from fastapi import FastAPI

app = FastAPI()

students = []

@app.get("/")
def CheckHealth():
    return {"message": "App is working"}


@app.post("/add")
def AddStudent(id: int, name: str, rollno: int):
    
    student = {
        "id": id,
        "name": name,
        "rollno": rollno
    }
    
    students.append(student)
    return {
        "message" : "Student added",
        "data": student
    }
    