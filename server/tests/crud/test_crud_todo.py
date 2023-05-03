from server.crud import crud_todo as crud 

todo_list_id:    int  = 0

def test_todo_create_list():
    global todo_list_id

    data = crud.todo.create_list('test-list')
    todo_list_id    = data['todo_id']

    assert data['todo_id'] == todo_list_id
    assert data['name']    == 'test-list'
    assert data['tasks']   == None

def test_todo_get_list():
    data = crud.todo.get_list(todo_list_id)

    assert data['todo_id'] == todo_list_id
    assert data['name']    == 'test-list'
    assert data['tasks']   == None

def test_todo_get_tasks_no_tasks():
    data = crud.todo.get_tasks(todo_list_id)

    assert data['tasks']   == None 

def test_todo_add_task():
    data = crud.todo.add_task(todo_list_id, 'test-task1')
    # data = crud.todo.add_task(todo_list_id, {"test-task2": False})
    assert data['todo_id'] == todo_list_id
    assert data['name'] == 'test-list'
    # assert data['tasks'] == {"test-task1": True}
    print(data)

def test_todo_get_tasks_one_task():
    data = crud.todo.get_tasks(todo_list_id)

    print(data)

def test_todo_delete_list():
    print(todo_list_id)
    assert crud.todo.delete_list(todo_list_id) is not None