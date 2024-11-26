from typing import Optional
from pydantic import BaseModel


class MenuItemBase(BaseModel):
    dish_name: str
    ingredients: str  # Comma-separated string or JSON in the database
    price: float
    calories: Optional[int] = None
    food_category: Optional[str] = None  # E.g., "Appetizer", "Main Course", etc.


class MenuItemCreate(MenuItemBase):
    pass


class MenuItemUpdate(BaseModel):
    dish_name: Optional[str] = None
    ingredients: Optional[str] = None
    price: Optional[float] = None
    calories: Optional[int] = None
    food_category: Optional[str] = None


class MenuItem(MenuItemBase):
    id: int

    class Config:
        orm_mode = True
