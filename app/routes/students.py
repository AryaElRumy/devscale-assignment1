from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from ..database import Student, get_db_session

students_router = APIRouter(prefix="/students")


@students_router.get("/")
def get_students(db: Session = Depends(get_db_session)):
    students = db.exec(select(Student)).all()
    return students
