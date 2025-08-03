from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from ..database import Student, get_db_session
from ..schema import RegisterStudent

students_router = APIRouter(prefix="/students", tags=["Students"])


@students_router.get("/")
def get_students(db: Session = Depends(get_db_session)):
    students = db.exec(select(Student)).all()
    return students


@students_router.post("/register")
def register_student(student: RegisterStudent, db: Session = Depends(get_db_session)):
    new_student = Student(
        name=student.name, grade=student.grade, address=student.address
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student
