from fastapi import FastAPI, HTTPException

from mosaic_v1.models import Menu, OrderResponse, Order, Pizza
from mosaic_v1.seeds import menu

app = FastAPI()


@app.get("/menu", response_model=Menu)
async def get_menu():
    return menu


@app.post("/order", response_model=OrderResponse)
async def place_order(order: Order):
    total_price = 0
    itemized_order = []

    for item in order.items:
        menu_item = next(
            (p for p in menu.classic_pizzas + menu.specialty_pizzas if p.name.lower() == item.item_name.lower()), None)
        if not menu_item:
            menu_item = next(
                (i for i in menu.sides + menu.drinks + menu.desserts if i.name.lower() == item.item_name.lower()), None)

        if not menu_item:
            if item.item_name.lower() == "build your own":
                menu_item = menu.build_your_own
            else:
                raise HTTPException(status_code=400, detail=f"Invalid item: {item.item_name}")

        if not menu_item.available:
            raise HTTPException(status_code=400, detail=f"{menu_item.name} is not available")

        price = menu_item.price
        if isinstance(menu_item, Pizza) or item.item_name.lower() == "build your own":
            if item.additional_ingredients:
                price += len(item.additional_ingredients) * 1.5  # $1.50 per additional topping

        item_total = price * item.quantity
        itemized_order.append({
            "name": menu_item.name,
            "quantity": item.quantity,
            "price": price,
            "total": item_total,
            "additional_ingredients": item.additional_ingredients
        })
        total_price += item_total

    return OrderResponse(items=itemized_order, total_price=total_price)


@app.patch("/menu/{item_type}/{item_name}")
async def update_item_availability(item_type: str, item_name: str, available: bool):
    if item_type == "build_your_own":
        menu.build_your_own.available = available
        return {"message": "Build Your Own pizza availability updated"}

    item_list = getattr(menu, item_type, None)
    if not item_list:
        raise HTTPException(status_code=404, detail="Invalid item type")

    item = next((i for i in item_list if i.name.lower() == item_name.lower()), None)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    item.available = available
    return {"message": "Item availability updated"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("mosaic_v1.pizzeria_api:app", host="0.0.0.0", port=8002, reload=True)
