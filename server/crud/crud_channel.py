from fastapi import HTTPException, status

from sb.sb_init import sb_client
from crud.crud_todo import todo

class CRUDChannel():
    __Table = 'Channel'
    __Id_column = 'channel_id'
    __Name_column = 'channel_name'
    __Users_column = 'channel_users'
    __ToDos_column = 'channel_todos'

    def get_channel(self, channel_id: int):
        try:
            data = sb_client.table(self.__Table).select('*').eq(self.__Id_column, channel_id).execute()
        except:
            raise HTTPException(detail = 'Error while getting channel', status_code = status.HTTP_404_NOT_FOUND)
        
        # Channel does not exist, data is an empty list
        if not data.data:
            return status.HTTP_404_NOT_FOUND
        
        return data.data[0]

    def create_channel(self, channel_name: str):
        try:
            data = sb_client.table(self.__Table).insert({self.__Name_column: channel_name}).execute()
            return data.data[0][self.__Id_column]
        except:
            raise HTTPException(detail = 'Error while creating Channel', status_code = status.HTTP_404_NOT_FOUND)

    def delete_channel(self, channel_id: int):
        if type(channel_id) is not int: raise TypeError
        
        try:
            sb_client.table(self.__Table).delete().eq(self.__Id_column, channel_id).execute()
            return status.HTTP_204_NO_CONTENT
        except:
            raise HTTPException(detail = 'Error in deleting channel. Channel not found', status_code = status.HTTP_404_NOT_FOUND)

    def modify_channel_name(self, channel_id: int, new_channel_name: str):
        try:
            sb_client.table(self.__Table).update({self.__Name_column: new_channel_name}).eq(self.__Id_column, channel_id).execute()
            return status.HTTP_204_NO_CONTENT
        except:
            raise HTTPException(detail = 'Channel not found', status_code = status.HTTP_404_NOT_FOUND)

    def get_users(self, channel_id: int):
        try:
            data = sb_client.table(self.__Table).select(self.__Users_column).eq(self.__Id_column, channel_id).execute()
            return data.data[0][self.__Users_column]
        except:
            raise HTTPException(detail = 'Channel not found', status_code = status.HTTP_404_NOT_FOUND)

    def add_user(self, channel_id: int, user_id: int):
        user_list = self.get_users(channel_id)
        
        # If there are no users, init an empty list
        if user_list is None: user_list = []
        
        # If a user is already in the list, return with 409_CONFLICT status
        if user_id not in user_list:
            user_list.append(user_id)
        else:
            return status.HTTP_409_CONFLICT
        
        try:
            sb_client.table(self.__Table).update({self.__Users_column: user_list}).eq(self.__Id_column, channel_id).execute()
            return status.HTTP_204_NO_CONTENT
        except:
            raise HTTPException(detail = 'Error in adding user', status_code = status.HTTP_404_NOT_FOUND)

    def remove_user(self, channel_id: int, user_id: int):
        user_list = self.get_users(channel_id)

        if user_list == None or user_id not in user_list :
            return status.HTTP_409_CONFLICT
        else:
            user_list.remove(user_id)
        
        try:
            sb_client.table(self.__Table).update({self.__Users_column: user_list}).eq(self.__Id_column, channel_id).execute()
            return status.HTTP_204_NO_CONTENT
        except:
            raise HTTPException(detail = 'Task not found', status_code = status.HTTP_404_NOT_FOUND)
        
    def get_todos(self, channel_id: int):
        try:
            data = sb_client.table(self.__Table).select(self.__ToDos_column).eq(self.__Id_column, channel_id).execute()
            return data.data[0][self.__ToDos_column]
        except:
            raise HTTPException(detail = 'Channel not found', status_code = status.HTTP_404_NOT_FOUND)

    def add_todo(self, channel_id: int, todo_id: int):

        todo_list = self.get_todos(channel_id)
        
        # If there are no users, init an empty list
        if todo_list is None: todo_list = []
        
        # If a user is already in the list, return with 409_CONFLICT status
        if todo_id not in todo_list:
            todo_list.append(todo_id)
        else:
            return status.HTTP_409_CONFLICT
        
        try:
            sb_client.table(self.__Table).update({self.__ToDos_column: todo_list}).eq(self.__Id_column, channel_id).execute()
            return status.HTTP_204_NO_CONTENT
        except:
            raise HTTPException(detail = 'Error in adding ToDo list', status_code = status.HTTP_404_NOT_FOUND)

    def remove_todo(self, channel_id: int, todo_id: int):
        todo_list = self.get_todos(channel_id)

        if todo_list == None or todo_id not in todo_list :
            return status.HTTP_409_CONFLICT
        else:
            todo_list.remove(todo_id)
        
        try:
            sb_client.table(self.__Table).update({self.__ToDos_column: todo_list}).eq(self.__Id_column, channel_id).execute()
            return status.HTTP_204_NO_CONTENT
        except:
            raise HTTPException(detail = 'ToDo list not found', status_code = status.HTTP_404_NOT_FOUND)

channel = CRUDChannel()