def add_task(task: str) -> str:
    todo_list.append(task)
    return f"Task '{task}' added to your TODO list."

def get_tasks() -> list:
    return todo_list
