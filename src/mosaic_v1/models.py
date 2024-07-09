from enum import Enum

from pydantic import BaseModel
from typing import List, Optional, Dict


class PizzaSize(str, Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"


class MenuItem(BaseModel):
    name: str
    description: str
    price: float
    available: bool = True


class Pizza(MenuItem):
    size: PizzaSize = PizzaSize.MEDIUM


class BuildYourOwn(MenuItem):
    base_price: float
    toppings: List[str] = []


class Side(BaseModel):
    name: str
    description: str
    price: float


class Drink(BaseModel):
    name: str
    description: str
    price: float


class Dessert(BaseModel):
    name: str
    description: str
    price: float


class Menu(BaseModel):
    pizzas: Dict[str, Pizza]
    build_your_own: BuildYourOwn
    sides: Dict[str, Side]
    drinks: Dict[str, Drink]
    desserts: Dict[str, Dessert]


class OrderItem(BaseModel):
    item_name: str
    quantity: int
    size: Optional[PizzaSize] = None
    toppings: Optional[List[str]] = None


class Order(BaseModel):
    items: List[OrderItem]


class OrderResponse(BaseModel):
    items: List[Dict[str, any]]
    total_price: float
