FILEPATH = "todos.txt"

def get_Todos(path = FILEPATH):
    with open(path, "r") as file:
        todos_raw = file.readlines()
        todos_clean = [item.strip("\n") for item in todos_raw]
    return todos_clean


def set_Todos(save_todos, path = FILEPATH):
    lb_todos = [f"{item}\n" for item in save_todos]
    with open(path, "w") as file:
        file.writelines(lb_todos)

