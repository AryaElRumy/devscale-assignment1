from pydantic import BaseModel


class RegisterStudent(BaseModel):
    name: str
    grade: int
    address: str


class ViewStudents(BaseModel):
    name: str
    grade: int


class UpdateStudent(RegisterStudent):
    pass
