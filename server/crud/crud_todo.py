from server.supabase.supabase_init import supabase

class CRUDToDo():
    __Table = "ToDo"

    def get_list(self, list_id: int):
        data = supabase.table(self.__Table).select("*").eq("todo_id", list_id).execute()
        return data.data[0]

    def create_list(self, list_name: str):
        data = supabase.table(self.__Table).insert({"name": list_name}).execute()
        return data.data[0]
    
    def delete_list(self, list_id: int):
        data = supabase.table(self.__Table).delete().eq("todo_id", list_id).execute()
        return data.data[0]

    def modify_list(self, list_name: str):
        pass

    def get_tasks(self, list_id: int):
        data = supabase.table(self.__Table).select("tasks").eq("todo_id", list_id).execute()
        return data.data[0]

    def add_task(self, list_id: int, task_name: str):
        prev_task_list = self.get_tasks(list_id)
        new_task_list = { task_name: False}
        data = supabase.table(self.__Table).update({"tasks": new_task_list}).eq("todo_id", list_id).execute()
        return data.data[0]
    
    def delete_task(self, list_name: str, task_name: str):
        pass

    def modify_task(self, list_name: str, task_name: str):
        pass

    def set_task_status(self, list_name: str, task_name: str, status: bool):
        pass

todo = CRUDToDo()