from fastapi import FastAPI, APIRouter
from models import Todo
from database import todos


router = APIRouter(prefix="/todos")

@router.get("/")
def read_todos():
    return todos

@router.post("/")
def create_todo(todo: Todo):
    todos.append(todo)
    return todo

@router.put("/{todo_id}")
def update_todo(todo_id: int, todo: Todo):
    for index, old_todo in enumerate(todos):
        if old_todo.id == todo_id:
            todos[index] = todo
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@router.delete("/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")
