import csv

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