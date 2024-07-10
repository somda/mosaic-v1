from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 12)
        self.cell(0, 10, "Tona Pizza Menu", 0, new_x="LMARGIN", new_y="NEXT", align="C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.cell(
            0, 10, f"Page {self.page_no()}", 0, new_x="RIGHT", new_y="TOP", align="C"
        )

    def chapter_title(self, title):
        self.set_font("Helvetica", "B", 12)
        self.cell(0, 10, title, 0, new_x="LMARGIN", new_y="NEXT", align="L")
        self.ln(5)

    def chapter_body(self, body):
        self.set_font("Helvetica", "", 12)
        self.multi_cell(0, 10, body)
        self.ln()


def create_menu_pdf():
    menu = {
        "Pizzas": [
            {
                "name": "Margherita",
                "price": "$8.99",
                "description": "Classic pizza with fresh tomatoes, mozzarella, and basil.",
            },
            {
                "name": "Pepperoni",
                "price": "$9.99",
                "description": "Delicious pizza topped with pepperoni and mozzarella cheese.",
            },
            {
                "name": "Hawaiian",
                "price": "$10.99",
                "description": "A tropical mix of ham, pineapple, and mozzarella cheese.",
            },
            {
                "name": "BBQ Chicken",
                "price": "$11.99",
                "description": "Savory BBQ sauce with grilled chicken, red onions, and cilantro.",
            },
            {
                "name": "Veggie",
                "price": "$9.99",
                "description": "Loaded with bell peppers, onions, olives, and mushrooms.",
            },
        ],
        "Drinks": [
            {
                "name": "Coke",
                "price": "$1.99",
                "description": "Refreshing classic Coca-Cola.",
            },
            {
                "name": "Sprite",
                "price": "$1.99",
                "description": "Lemon-lime flavored soft drink.",
            },
            {
                "name": "Water",
                "price": "$1.50",
                "description": "Bottled mineral water.",
            },
        ],
        "Sides": [
            {
                "name": "Garlic Bread",
                "price": "$3.99",
                "description": "Toasted bread with garlic butter and herbs.",
            },
            {
                "name": "Chicken Wings",
                "price": "$5.99",
                "description": "Spicy chicken wings served with dipping sauce.",
            },
            {
                "name": "Salad",
                "price": "$4.99",
                "description": "Fresh garden salad with a variety of vegetables.",
            },
        ],
    }

    pdf = PDF()
    pdf.add_page()

    for category, items in menu.items():
        pdf.chapter_title(category)
        for item in items:
            body = f"{item['name']} - {item['price']}\n{item['description']}\n"
            pdf.chapter_body(body)

    pdf.output("Tona_Pizza_Menu.pdf")


if __name__ == "__main__":
    create_menu_pdf()
