from enum import Enum

from pydantic import BaseModel
from typing import List, Optional, Dict, Union


class Ingredient(str, Enum):
    TOMATO_SAUCE = "Tomato sauce"
    MOZZARELLA = "mozzarella"
    BASIL = "basil"
    PEPPERONI = "pepperoni"
    HAM = "ham"
    PINEAPPLE = "pineapple"
    BELL_PEPPERS = "bell peppers"
    ONIONS = "onions"
    MUSHROOMS = "mushrooms"
    SAUSAGE = "sausage"
    BACON = "bacon"
    BBQ_SAUCE = "BBQ sauce"
    GRILLED_CHICKEN = "grilled chicken"
    RED_ONIONS = "red onions"


class MenuItem(BaseModel):
    name: str
    description: str
    price: float
    available: bool = True


class Pizza(MenuItem):
    ingredients: List[Ingredient]


class BuildYourOwn(MenuItem):
    pass


class Side(MenuItem):
    pass


class Drink(MenuItem):
    pass


class Dessert(MenuItem):
    pass


class Menu(BaseModel):
    classic_pizzas: List[Pizza]
    specialty_pizzas: List[Pizza]
    build_your_own: BuildYourOwn
    sides: List[Side]
    drinks: List[Drink]
    desserts: List[Dessert]


class OrderItem(BaseModel):
    item_name: str
    quantity: int
    additional_ingredients: Optional[List[Ingredient]] = None


class Order(BaseModel):
    items: List[OrderItem]


class OrderResponse(BaseModel):
    items: List[Dict[str, Union[Pizza, BuildYourOwn, Side, Drink, Dessert]]]
    total_price: float
