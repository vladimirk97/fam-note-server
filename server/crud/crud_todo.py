from fastapi import HTTPException, status

from sb.sb_init import sb_client

class CRUDToDo():
    __Table = "ToDo"

    def get_list(self, list_id: int):
        try:
            data = sb_client.table(self.__Table).select("*").eq("todo_id", list_id).execute()
            return data.data[0]
        except:
            raise HTTPException(detail = 'ToDo list not found', status_code = status.HTTP_404_NOT_FOUND)

    def create_list(self, list_name: str) -> int:
        try:
            data = sb_client.table(self.__Table).insert({"name": list_name}).execute()
            return data.data[0]['todo_id']
        except:
            raise HTTPException(detail = 'Error while creating ToDo list', status_code = status.HTTP_404_NOT_FOUND)
    
    def delete_list(self, list_id: int):
        try:
            sb_client.table(self.__Table).delete().eq("todo_id", list_id).execute()
            return status.HTTP_204_NO_CONTENT
        except:
            raise HTTPException(detail = 'ToDo list not found', status_code = status.HTTP_404_NOT_FOUND)

    def modify_list_name(self, list_id: int, new_list_name: str):
        try:
            sb_client.table(self.__Table).update({"name": new_list_name}).eq("todo_id", list_id).execute()
            return status.HTTP_204_NO_CONTENT
        except:
            raise HTTPException(detail = 'ToDo list not found', status_code = status.HTTP_404_NOT_FOUND)

    def get_tasks(self, list_id: int) -> dict:
        try:
            data = sb_client.table(self.__Table).select("tasks").eq("todo_id", list_id).execute()
            return data.data[0]
        except:
            raise HTTPException(detail = 'ToDo list not found', status_code = status.HTTP_404_NOT_FOUND)

    def add_task(self, list_id: int, task_name: str):
        prev_task_list = self.get_tasks(list_id).get('tasks', {}) or {}
        new_task_list = {**prev_task_list, task_name: False}
        try:
            sb_client.table(self.__Table).update({"tasks": new_task_list}).eq("todo_id", list_id).execute()
            return status.HTTP_204_NO_CONTENT
        except:
            raise HTTPException(detail = 'Error while adding task', status_code = status.HTTP_404_NOT_FOUND)
    
    def delete_task(self, list_id: int, task_name: str) -> bool | Exception:
        task_list = self.get_tasks(list_id).get('tasks', {}) or {}
        try:
            del task_list[task_name]
            sb_client.table(self.__Table).update({"tasks": task_list}).eq("todo_id", list_id).execute()
            return status.HTTP_204_NO_CONTENT
        except:
            raise HTTPException(detail = 'Task not found', status_code = status.HTTP_404_NOT_FOUND)

    def modify_task_name(self, list_id: int, task_name: str, new_task_name: str):
        task_list = self.get_tasks(list_id).get('tasks', {}) or {}
        try:
            task_list[new_task_name] = task_list.pop(task_name) 
            sb_client.table(self.__Table).update({"tasks": task_list}).eq("todo_id", list_id).execute()
            return status.HTTP_204_NO_CONTENT
        except KeyError:
            raise HTTPException(detail = 'Task not found', status_code = status.HTTP_404_NOT_FOUND)
        except:
            raise HTTPException(detail = 'Error while changing task name', status_code = status.HTTP_404_NOT_FOUND)

    def set_task_status(self, list_id: int, task_name: str, set_status: bool):
        task_list = self.get_tasks(list_id).get('tasks', {}) or {}
        try:
            task_list[task_name] = set_status
            sb_client.table(self.__Table).update({"tasks": task_list}).eq("todo_id", list_id).execute()
            return status.HTTP_204_NO_CONTENT
        except KeyError:
            raise HTTPException(detail = 'Task not found', status_code = status.HTTP_404_NOT_FOUND)
        except:
            raise HTTPException(detail = 'Error while changing task status', status_code = status.HTTP_404_NOT_FOUND)

todo = CRUDToDo()