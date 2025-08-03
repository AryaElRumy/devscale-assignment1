from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from starlette.status import HTTP_404_NOT_FOUND

from ..database import Student, get_db_session
from ..schema import RegisterStudent, UpdateStudent, ViewStudents

students_router = APIRouter(prefix="/students", tags=["Students"])


@students_router.get("/", response_model=List[ViewStudents])
def get_students(db: Session = Depends(get_db_session)):
    students = db.exec(select(Student)).all()
    return students


@students_router.get("/{student_id}", response_model=ViewStudents)
def get_student(student_id: int, db: Session = Depends(get_db_session)):
    student = db.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Student not found")
    return student


@students_router.post("/", response_model=Student)
def register_student(student: RegisterStudent, db: Session = Depends(get_db_session)):
    new_student = Student(
        name=student.name, grade=student.grade, address=student.address
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


@students_router.put("/{student_id}", response_model=ViewStudents)
def update_student(
    student_id: int,
    update_student: UpdateStudent,
    db: Session = Depends(get_db_session),
):
    student = db.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Student not found")

    update_student = update_student.dict(exclude_unset=True)
    for field, value in update_student.items():
        setattr(student, field, value)

    db.add(student)
    db.commit()
    db.refresh(student)

    return student


@students_router.post("/{student_id}")
def unregister_student(student_id: int, db: Session = Depends(get_db_session)):
    student = db.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Student not found")
    db.delete(student)
    db.commit()

    return {"message": "Student unregistered succesfully"}
