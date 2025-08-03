from typing import Optional

from pydantic import BaseModel


class RegisterStudent(BaseModel):
    name: str
    grade: int
    address: Optional[str] | None


class ViewStudents(BaseModel):
    name: str
    grade: int


class UpdateStudent(RegisterStudent):
    pass
