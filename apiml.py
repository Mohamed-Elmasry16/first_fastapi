from fastapi import FastAPI , Query
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


class Student(BaseModel):
    id:int 
    name :str
    grade: int 

app = FastAPI()

# Allow requests from your local HTML file
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # in development you can allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

students =[Student(id=1,name="hassan ali" ,grade= 4),
           Student(id=2,name="mohamed ali" , grade=5),
           Student(id=3,name="hassana mohamed" ,grade=5)]


@app.get("/student/")
async def read_students():
    return students

@app.post("/student/")
async def add_students(new_student : Student):
    students.append(new_student)
    return new_student

@app.put("/student{stu_id}/")
async def update_students(stu_id:int, update_student : Student):
        for index , stu  in enumerate(students):
            if stu.id == stu_id:
                students[index] = update_student
                return update_student
        return {"error" : "student dont exist "}
    
@app.delete("/student{stu_id}/")
async def delete_students(stu_id:int, delete_student : Student):
        for index , stu  in enumerate(students):
            if stu.id == stu_id:
                del students[index] 
                return {"message": "student deleted "}
        return {"error" : "student dont exist "}
        
 

         




