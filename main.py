from fastapi import FastAPI

app = FastAPI()

students = []

@app.get("/")
def home():
    return {"message" : "Student Management System Running"}

@app.get("/students")
def get_students():
    return students

@app.post("/create_student")
def add_student(id: int, name: str, age: int, course: str):
    
    student = {
        "id": id,
        "name": name,
        "age": age,
        "course": course
    }
    
    students.append(student)
    
    return {
        "message" : "Student added successfull",
        "status code" : 200,
        "data": student
    }
    

@app.get("/student/{id}")
def get_by_id(id: int):

    for student in students:

        if student["id"] == id:

            return {
                "message": "Student found",
                "data": student
            }

    return {
        "message": "Student not found"
    }
    

@app.put("/update_student/{id}")
def update_student(id: int, new_name: str):
    
    for student in students:
        if student["id"] == id:
            
            student["name"] = new_name
            return {
                "message" : "Data updated successfully",
                "data": student
            }
    return {"message" : "Student Not found"}


@app.delete("/delete/{id}")
def delete_student(id: int):
    
    for student in students:
        if student["id"] == id:
            
            students.remove(student)
            return {
                "message" : "deleted successfully"
            }
            
    return {"message": "Student not found"}