import csv


csv_path = "menu.csv"
def read_menu_from_csv(csv_path):
    menu = {}
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            category = row['category']
            if category not in menu:
                menu[category] = []
            menu[category].append({
                'name': row['name'],
                'price': row['price'],
                'description': row['description']
            })
    return menu


# def format_menu_for_prompt(menu):
#     formatted_menu = ""
#     for category, items in menu.items():
#         formatted_menu += f"{category}:\n"
#         for item in items:
#             formatted_menu += f"- {item['name']} ({item['price']}): {item['description']}\n"
#     return formatted_menu



# # # Test menu
# if __name__ == "__main__":
#     csv_path = 'menu.csv'
#     menu = read_menu_from_csv(csv_path)
#     print(menu)


# # Test formatted menu
# if __name__ == "__main__":
#     csv_path = 'menu.csv'
#     menu = read_menu_from_csv(csv_path)
#     formatted_menu = format_menu_for_prompt(menu)
#     print(formatted_menu)