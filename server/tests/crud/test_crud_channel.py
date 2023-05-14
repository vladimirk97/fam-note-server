import pytest
from fastapi import status
from crud import crud_channel as crud 

channel_id: int  = 0

def test_get_channel_that_doesnt_exist():
    assert crud.channel.get_channel(channel_id) is status.HTTP_404_NOT_FOUND
    
def test_get_channel_bad_input():
    with pytest.raises(Exception):
        assert crud.channel.get_channel('invalid-input')

def test_create_channel():
    global channel_id
    
    data = crud.channel.create_channel('test-channel')
    channel_id = data
    assert data != None

# def test_create_channel_bad_input():
#     with pytest.raises(Exception):
#         assert crud.channel.create_channel(111)

def test_get_channel():
    data = crud.channel.get_channel(channel_id)
    assert data['channel_name'] == 'test-channel'

def test_get_user_no_users():
    assert crud.channel.get_users(channel_id) is None

def test_remove_user_no_users():
    assert crud.channel.remove_user(channel_id, 12344) is status.HTTP_409_CONFLICT

def test_add_user():
    assert crud.channel.add_user(channel_id, 12345) is status.HTTP_204_NO_CONTENT
    assert crud.channel.add_user(channel_id, 12345) is status.HTTP_409_CONFLICT
    assert crud.channel.add_user(channel_id, 12346) is status.HTTP_204_NO_CONTENT
    
    data = crud.channel.get_users(channel_id)
    assert data == [12345, 12346]

def test_remove_user():
    assert crud.channel.remove_user(channel_id, 12345) is status.HTTP_204_NO_CONTENT
    assert crud.channel.remove_user(channel_id, 12344) is status.HTTP_409_CONFLICT

    data = crud.channel.get_users(channel_id)
    assert data == [12346]

def test_get_todos_no_todos():
    assert crud.channel.get_todos(channel_id) is None

def test_remove_todo_no_todos():
    assert crud.channel.remove_todo(channel_id, 111) is status.HTTP_409_CONFLICT

def test_add_todo():
    assert crud.channel.add_todo(channel_id, 111) is status.HTTP_204_NO_CONTENT
    assert crud.channel.add_todo(channel_id, 111) is status.HTTP_409_CONFLICT
    assert crud.channel.add_todo(channel_id, 222) is status.HTTP_204_NO_CONTENT
    
    data = crud.channel.get_todos(channel_id)
    assert data == [111, 222]

def test_add_todo_bad_input():
    with pytest.raises(Exception):
       assert crud.channel.add_todo('invalid-input', 111)
     
    with pytest.raises(Exception):
       assert crud.channel.add_todo(channel_id, 'invalid-input')
     
def test_remove_todo():
    assert crud.channel.remove_todo(channel_id, 111) is status.HTTP_204_NO_CONTENT
    assert crud.channel.remove_todo(channel_id, 333) is status.HTTP_409_CONFLICT

    data = crud.channel.get_todos(channel_id)
    assert data == [222]

def test_modify_channel_name():
    data = crud.channel.modify_channel_name(channel_id, 'test-channel1')
    assert data == status.HTTP_204_NO_CONTENT

    data = crud.channel.get_channel(channel_id)
    assert data['channel_name'] == 'test-channel1' 

def test_modify_channel_bad_input():
    with pytest.raises(Exception):
        assert crud.channel.modify_channel_name('invalid-input', 'test-channel1')

    with pytest.raises(Exception):
        assert crud.channel.modify_channel_name('invalid-input')

def test_delete_channel():
    data = crud.channel.delete_channel(channel_id)
    assert data == status.HTTP_204_NO_CONTENT

def test_delete_channel_bad_input():
    with pytest.raises(TypeError):
        assert crud.channel.delete_channel('invalid-input')