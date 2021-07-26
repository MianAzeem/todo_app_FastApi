from sqlalchemy import Column, Integer, String
from core.models.db import Base
from sqlalchemy.orm import Session


class TODOS(Base):
   __tablename__ = "todo"

   id = Column(Integer, primary_key=True, index=True, autoincrement=True)
   title = Column(String, index=True)
   description = Column(String, index=True)

from typing import List, Optional
from pydantic import BaseModel


class ItemBase(BaseModel):

   title: str
   description: Optional[str] = None

   class Config:
      orm_mode = True


class CreateItem(ItemBase):
   id: int
   title: str
   description: Optional[str] = None


def get_item_by_id(db: Session, item_id: int):
   return db.query(TODOS).filter(TODOS.id == item_id).first()


def create_todo_item(db: Session, todo_item: CreateItem):
   db_todo_item = TODOS(**todo_item.dict())
   db.add(db_todo_item)
   db.commit()
   db.refresh(db_todo_item)
   return db_todo_item

def update_todo_item(db: Session, todo_item: ItemBase, item_id: int):
   item = db.query(TODOS).filter(TODOS.id == item_id).first()
   item.title = todo_item.title
   item.description = todo_item.description
   db.commit()
   db.refresh(item)
   return item

def delete_todo(db: Session, item_id: int):
   todo = db.query(TODOS).filter(TODOS.id == item_id).first()
   db.delete(todo)
   db.commit()

def todos_list(db: Session):
   return db.query(TODOS).all()
