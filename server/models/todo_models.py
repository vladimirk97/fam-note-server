from pydantic import BaseModel

class ToDoBase(BaseModel):
    todo_name: str
    todo_tasks: dict | None = None

class ToDoList(ToDoBase):
    todo_id: int
    created_at: str

