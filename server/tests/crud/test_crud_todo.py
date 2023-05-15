import pytest
from fastapi import status
from crud import crud_todo as crud 

todo_list_id: int  = 0

Id_column = 'todo_id'
Name_column = 'todo_name'
Tasks_column = 'todo_tasks'


def test_todo_create_list():
    global todo_list_id
    data = crud.todo.create('test-list')
    todo_list_id = data
    assert data == todo_list_id

def test_todo_get_list():
    data = crud.todo.get(todo_list_id)
    assert data[Id_column] == todo_list_id
    assert data[Name_column]    == 'test-list'
    assert data[Tasks_column]   == None

def test_todo_modify_list_name():
    data = crud.todo.modify_name(todo_list_id, 'test-list1')
    assert data == status.HTTP_204_NO_CONTENT

    data = crud.todo.get(todo_list_id)
    assert data[Name_column] == 'test-list1'   
    
def test_todo_get_tasks_no_tasks():
    data = crud.todo.get_tasks(todo_list_id)
    assert data[Tasks_column]   == None 

def test_todo_add_task():
    data = crud.todo.add_task(todo_list_id, 'test-task1')
    assert data == status.HTTP_204_NO_CONTENT

def test_todo_add_second_task():
    data = crud.todo.add_task(todo_list_id, 'test-task2')
    assert data == status.HTTP_204_NO_CONTENT

def test_todo_get_tasks():
    data = crud.todo.get_tasks(todo_list_id)
    assert data[Tasks_column] == {'test-task1': False, 'test-task2': False}

def test_delete_task():
    data = crud.todo.delete_task(todo_list_id, 'test-task2')
    assert data == status.HTTP_204_NO_CONTENT

    data = crud.todo.get_tasks(todo_list_id)
    assert data[Tasks_column] == {'test-task1': False}

def test_modify_task_name():
    data = crud.todo.modify_task_name(todo_list_id, 'test-task1', 'test-task3')
    assert data == status.HTTP_204_NO_CONTENT

    data = crud.todo.get_tasks(todo_list_id)
    assert data[Tasks_column] == {'test-task3': False}

def test_set_task_status():
    data = crud.todo.set_task_status(todo_list_id, 'test-task3', True)
    assert data == status.HTTP_204_NO_CONTENT

    data = crud.todo.get_tasks(todo_list_id)
    assert data[Tasks_column] == {'test-task3': True}

def test_todo_delete_list():
    data = crud.todo.delete(todo_list_id)
    assert data == status.HTTP_204_NO_CONTENT

def test_todo_delete_list_fail():
    with pytest.raises(Exception):
        assert crud.todo.delete("invalid id")