from fastapi import FastAPI, Depends, HTTPException
from core.models.todo import (
    create_todo_item, delete_todo, get_item_by_id,todos_list, update_todo_item, ItemBase,
    CreateItem
)
from typing import List
from core.models.db import SessionLocal
from sqlalchemy.orm import Session

def create_app():
    app = FastAPI()

    return app


app = create_app()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/item/all", response_model=List[ItemBase])
def read_items(db: Session = Depends(get_db)):
    """
    returns all todos
    """
    return todos_list(db=db)


@app.get("/item/{item_id}", response_model=ItemBase)
def read_item(item_id: int, db: Session = Depends(get_db)):
    """
    get and returns item by id
    """
    item = get_item_by_id(db, item_id)
    if item:
        return item
    else:
        raise HTTPException(status_code=422, detail="todo item with given id not found")


@app.post("/item", response_model=CreateItem)
def create_item(todo_item: CreateItem, db: Session = Depends(get_db)):
    """
    create and returns todo item
    """
    try:
        return create_todo_item(db=db, todo_item=todo_item)
    except:
        raise HTTPException(status_code=400, detail="bad request")


@app.put("/item/{item_id}", response_model=ItemBase)
def update_item(item_id: int, todo_item: ItemBase, db: Session = Depends(get_db)):
    """
    update a todo item by id
    returns updated todo item
    """
    try:
        return update_todo_item(db=db, todo_item=todo_item, item_id=item_id)
    except:
        raise HTTPException(status_code=422, detail="unprocessable entity.")


@app.delete("/item/{item_id}")
def delete_todo_item(item_id: int, db: Session = Depends(get_db)):
    """
    delete a todo item by id
    """
    try:
        delete_todo(db=db, item_id=item_id)
        return {"message": "TODO Deleted Successfully"}
    except:
        raise HTTPException(status_code=404, detail="TODO with given id is not found.")
