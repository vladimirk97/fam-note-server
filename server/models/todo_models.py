from pydantic import BaseModel

class ToDoBase(BaseModel):
    name: str
    tasks: dict | None = None

