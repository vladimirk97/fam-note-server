from server.supabase.supabase_init import supabase

class CRUDToDo():
    __Table = "ToDo"

    def create_list(self, list_name: str):
        data = supabase.table(self.__Table).insert({"name": list_name}).execute()
        return data.data[0]
    
    def get_list(self, list_id: int):
        data = supabase.table(self.__Table).select("todo_id").eq("todo_id", list_id).execute()
        return data.data[0]

    def delete_list(self, list_id: int):
        data = supabase.table(self.__Table).delete().eq("todo_id", list_id).execute()
        return data.data[0]

    def modify_list(self, list_name: str):
        pass

    def add_task(self, list_id: int, task_name: dict):
        data = supabase.table(self.__Table).update({"tasks": task_name}).eq("todo_id", list_id).execute()
        return data.data[0]
    
    def get_task(self, list_id: int, task_name: str):
        pass

    def delete_task(self, list_name: str, task_name: str):
        pass

    def modify_task(self, list_name: str, task_name: str):
        pass

    def set_task_status(self, list_name: str, task_name: str, status: bool):
        pass
    



    # def read(self):
    #     data = supabase.table("ToDo").select("*").eq("name", "Germany").execute()

todo = CRUDToDo()