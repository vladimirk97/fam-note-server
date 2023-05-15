from pydantic import BaseModel

class CreateToDo(BaseModel):
    todo_name: str

class ToDoId(BaseModel):
    todo_id: int