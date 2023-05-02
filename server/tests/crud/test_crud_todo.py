from server.crud import crud_todo as crud 

todo_list_id: int = 0

def test_todo_create():
    global todo_list_id
    data = crud.todo.create_list("test-list")
    todo_list_id = data['todo_id']

    assert data['todo_id'] == todo_list_id
    assert data['name'] == 'test-list'
    assert data['tasks'] == None
    print("Test: ToDo list create")

def test_todo_get():
    data = crud.todo.get_list(todo_list_id)
    print(data)

def test_todo_add_task():
    data = crud.todo.add_task(todo_list_id, {"test-task1": True})
    data = crud.todo.add_task(todo_list_id, {"test-task2": False})
    assert data['todo_id'] == todo_list_id
    assert data['name'] == 'test-list'
    # assert data['tasks'] == {"test-task1": True}
    print(data)
    print("Test: ToDo list add task")

def test_todo_delete():
    print(todo_list_id)
    assert crud.todo.delete_list(todo_list_id) is not None
    print("Test: ToDo list delete")