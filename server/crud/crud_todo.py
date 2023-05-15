from fastapi import HTTPException, status

from sb.sb_init import sb_client
from schemas.todo_schemas import CreateToDo, ToDoId

class CRUDToDo():
    __Table = 'ToDo'
    __Id_column = 'todo_id'
    __Name_column = 'todo_name'
    __Tasks_column = 'todo_tasks'

    def get(self, todo_id: int):
        try:
            data = sb_client.table(self.__Table).select('*').eq(self.__Id_column, todo_id).execute()
            return data.data[0]
        except:
            raise HTTPException(detail = 'ToDo list not found', status_code = status.HTTP_404_NOT_FOUND)

    def create(self, create_data: str) -> int:
        try:
            data = sb_client.table(self.__Table).insert({self.__Name_column: create_data}).execute()
            return data.data[0]['todo_id']
        except:
            raise HTTPException(detail = 'Error while creating ToDo list', status_code = status.HTTP_404_NOT_FOUND)
    
    def delete(self, todo_id: int):
        try:
            sb_client.table(self.__Table).delete().eq(self.__Id_column, todo_id).execute()
            return status.HTTP_204_NO_CONTENT
        except:
            raise HTTPException(detail = 'ToDo list not found', status_code = status.HTTP_404_NOT_FOUND)

    def modify_name(self, todo_id: int, new_list_name: str):
        try:
            sb_client.table(self.__Table).update({self.__Name_column: new_list_name}).eq(self.__Id_column, todo_id).execute()
            return status.HTTP_204_NO_CONTENT
        except:
            raise HTTPException(detail = 'ToDo list not found', status_code = status.HTTP_404_NOT_FOUND)

    def get_tasks(self, todo_id: int) -> dict:
        try:
            data = sb_client.table(self.__Table).select(self.__Tasks_column).eq(self.__Id_column, todo_id).execute()
            return data.data[0]
        except:
            raise HTTPException(detail = 'ToDo list not found', status_code = status.HTTP_404_NOT_FOUND)

    def add_task(self, todo_id: int, task_name: str):
        prev_task_list = self.get_tasks(todo_id).get(self.__Tasks_column, {}) or {}
        new_task_list = {**prev_task_list, task_name: False}
        try:
            sb_client.table(self.__Table).update({self.__Tasks_column: new_task_list}).eq(self.__Id_column, todo_id).execute()
            return status.HTTP_204_NO_CONTENT
        except:
            raise HTTPException(detail = 'Error while adding task', status_code = status.HTTP_404_NOT_FOUND)
    
    def delete_task(self, todo_id: int, task_name: str) -> bool | Exception:
        task_list = self.get_tasks(todo_id).get(self.__Tasks_column, {}) or {}
        try:
            del task_list[task_name]
            sb_client.table(self.__Table).update({self.__Tasks_column: task_list}).eq(self.__Id_column, todo_id).execute()
            return status.HTTP_204_NO_CONTENT
        except:
            raise HTTPException(detail = 'Task not found', status_code = status.HTTP_404_NOT_FOUND)

    def modify_task_name(self, todo_id: int, task_name: str, new_task_name: str):
        task_list = self.get_tasks(todo_id).get(self.__Tasks_column, {}) or {}
        try:
            task_list[new_task_name] = task_list.pop(task_name) 
            sb_client.table(self.__Table).update({self.__Tasks_column: task_list}).eq(self.__Id_column, todo_id).execute()
            return status.HTTP_204_NO_CONTENT
        except KeyError:
            raise HTTPException(detail = 'Task not found', status_code = status.HTTP_404_NOT_FOUND)
        except:
            raise HTTPException(detail = 'Error while changing task name', status_code = status.HTTP_404_NOT_FOUND)

    def set_task_status(self, todo_id: int, task_name: str, set_status: bool):
        task_list = self.get_tasks(todo_id).get(self.__Tasks_column, {}) or {}
        try:
            task_list[task_name] = set_status
            sb_client.table(self.__Table).update({self.__Tasks_column: task_list}).eq(self.__Id_column, todo_id).execute()
            return status.HTTP_204_NO_CONTENT
        except KeyError:
            raise HTTPException(detail = 'Task not found', status_code = status.HTTP_404_NOT_FOUND)
        except:
            raise HTTPException(detail = 'Error while changing task status', status_code = status.HTTP_404_NOT_FOUND)

todo = CRUDToDo()