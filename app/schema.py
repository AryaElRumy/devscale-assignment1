from pydantic import BaseModel


class RegisterStudent(BaseModel):
    name: str
    grade: int
    address: str
