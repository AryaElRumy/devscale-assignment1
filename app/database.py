import os
from typing import Optional

from dotenv import load_dotenv
from sqlmodel import Field, Session, SQLModel, create_engine

load_dotenv(override=True)

engine = create_engine(
    os.environ.get("DATABASE_URL", "sqlite///./data/student_data.db")
)


def get_db_session():
    with Session(engine) as session:
        yield session


class Student(SQLModel, table=True):
    student_id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    grade: int
    address: str
