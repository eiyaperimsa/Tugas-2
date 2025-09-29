from fastapi import APIRouter
from typing import  List
from modules.items.schema.schemas import Item, ResponseModel

router = APIRouter()
items: List[Item] = []

@router.post("/create/", response_model=ResponseModel)
def create_item(item: Item):
  items.append(item)
  # return item
  return {
    "success": True,
    "message": "New data successfully created",
    "data": item
  }