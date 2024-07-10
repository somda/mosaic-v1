from mosaic_v1.models import Menu, Pizza, BuildYourOwn, Side, Drink, Dessert, Ingredient

menu = Menu(
    classic_pizzas=[
        Pizza(name="Margherita", description="Tomato sauce, mozzarella, basil", price=12.99, ingredients=[Ingredient.TOMATO_SAUCE, Ingredient.MOZZARELLA, Ingredient.BASIL]),
        Pizza(name="Pepperoni", description="Tomato sauce, mozzarella, pepperoni", price=14.99, ingredients=[Ingredient.TOMATO_SAUCE, Ingredient.MOZZARELLA, Ingredient.PEPPERONI]),
        Pizza(name="Hawaiian", description="Tomato sauce, mozzarella, ham, pineapple", price=15.99, ingredients=[Ingredient.TOMATO_SAUCE, Ingredient.MOZZARELLA, Ingredient.HAM, Ingredient.PINEAPPLE]),
    ],
    specialty_pizzas=[
        Pizza(name="Veggie", description="Tomato sauce, mozzarella, bell peppers, onions, mushrooms", price=16.99, ingredients=[Ingredient.TOMATO_SAUCE, Ingredient.MOZZARELLA, Ingredient.BELL_PEPPERS, Ingredient.ONIONS, Ingredient.MUSHROOMS]),
        Pizza(name="Meat Lovers", description="Tomato sauce, mozzarella, pepperoni, sausage, bacon", price=17.99, ingredients=[Ingredient.TOMATO_SAUCE, Ingredient.MOZZARELLA, Ingredient.PEPPERONI, Ingredient.SAUSAGE, Ingredient.BACON]),
        Pizza(name="BBQ Chicken", description="BBQ sauce, mozzarella, grilled chicken, red onions", price=16.99, ingredients=[Ingredient.BBQ_SAUCE, Ingredient.MOZZARELLA, Ingredient.GRILLED_CHICKEN, Ingredient.RED_ONIONS]),
    ],
    build_your_own=BuildYourOwn(
        name="Build Your Own",
        description="Start with a classic crust and add your favorite toppings",
        price=10.99
    ),
    sides=[
        Side(name="Garlic Bread", description="Freshly baked bread with garlic butter", price=4.99),
        Side(name="Breadsticks", description="Soft, buttery breadsticks with dipping sauce", price=5.99),
    ],
    drinks=[
        Drink(name="Soda", description="Coke, Sprite, or Dr. Pepper", price=2.99),
        Drink(name="Iced Tea", description="Freshly brewed iced tea", price=2.99),
    ],
    desserts=[
        Dessert(name="Chocolate Cake", description="Rich, moist chocolate cake with chocolate frosting", price=5.99),
        Dessert(name="Tiramisu", description="Layers of coffee-soaked ladyfingers and mascarpone", price=6.99),
    ]
)
