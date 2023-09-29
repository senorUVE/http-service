from sqlmodel import SQLModel, Field
from typing import List

class File(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    columns: List[str]