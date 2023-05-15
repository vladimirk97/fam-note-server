from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from fastapi import APIRouter, status

from crud import crud_todo as crud
from schemas.todo_schemas import CreateToDo, ToDoId
from models.todo_models import ToDoList
router = APIRouter()

# Create ToDo list
@router.post('', include_in_schema = True)
async def create_todo(req_data: CreateToDo):
    try:
        todo_id = crud.todo.create(req_data.todo_name)
    except:
        raise HTTPException(detail = 'Error in creating ToDo list', status_code = status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    return JSONResponse(content = todo_id, status_code = status.HTTP_200_OK)

# Get ToDo list
@router.get('', include_in_schema = True)
async def get_todo(todo_id: int) -> ToDoList:
    try:
        todo_data = crud.todo.get(todo_id)
    except:
        raise HTTPException(detail = 'Error in fetching ToDo list', status_code = status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    return JSONResponse(content = todo_data, status_code = status.HTTP_200_OK)

# Delete ToDo list
@router.delete('', include_in_schema = True)
async def delete_todo(req_data: ToDoId):
    try:
        crud.todo.delete(req_data.todo_id)
    except:
        raise HTTPException(detail = 'Error in deleting ToDo list', status_code = status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    return JSONResponse(content = 'ToDo list deleted', status_code = status.HTTP_200_OK)