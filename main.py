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
    

@app.get("/getall")
def getAllStudents():
    return {
        "data": students
    }

@app.get("/student/{id}")
def getstudent(id:int):
    for student in students:

        if student["id"]==id:
          return{
            "data": students
          }
    return {
        "message":"data not found"
    }

@app.put("/update/{id}")
def updateStudent(id: int, name: str):
    for student in students:
        if student["id"] == id:
            student["name"] = name
            return{
                "data":students
            }
    return{
        "message":"id not foound"
    }