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