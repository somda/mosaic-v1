from mosaic_v1.models import Menu, Pizza, BuildYourOwn, Side, Drink, Dessert

menu = Menu(
    pizzas={
        "margherita": Pizza(
            name="Margherita",
            description="Tomato sauce, mozzarella, basil",
            price=12.99,
        ),
        "pepperoni": Pizza(
            name="Pepperoni",
            description="Tomato sauce, mozzarella, pepperoni",
            price=14.99,
        ),
        "hawaiian": Pizza(
            name="Hawaiian",
            description="Tomato sauce, mozzarella, ham, pineapple",
            price=15.99,
        ),
        "veggie": Pizza(
            name="Veggie",
            description="Tomato sauce, mozzarella, bell peppers, onions, mushrooms",
            price=16.99,
        ),
        "meat_lovers": Pizza(
            name="Meat Lovers",
            description="Tomato sauce, mozzarella, pepperoni, sausage, bacon",
            price=17.99,
        ),
        "bbq_chicken": Pizza(
            name="BBQ Chicken",
            description="BBQ sauce, mozzarella, grilled chicken, red onions",
            price=16.99,
        ),
    },
    build_your_own=BuildYourOwn(
        name="Build Your Own",
        description="Start with a classic crust and add your favorite toppings",
        price=10.99,
        base_price=10.99,
    ),
    sides={
        "garlic_bread": Side(
            name="Garlic Bread",
            description="Freshly baked bread with garlic butter",
            price=4.99,
        ),
        "breadsticks": Side(
            name="Breadsticks",
            description="Soft, buttery breadsticks with dipping sauce",
            price=5.99,
        ),
    },
    drinks={
        "soda": Drink(
            name="Soda", description="Coke, Sprite, or Dr. Pepper", price=2.99
        ),
        "iced_tea": Drink(
            name="Iced Tea", description="Freshly brewed iced tea", price=2.99
        ),
    },
    desserts={
        "chocolate_cake": Dessert(
            name="Chocolate Cake",
            description="Rich, moist chocolate cake with chocolate frosting",
            price=5.99,
        ),
        "tiramisu": Dessert(
            name="Tiramisu",
            description="Layers of coffee-soaked ladyfingers and mascarpone",
            price=6.99,
        ),
    },
)
