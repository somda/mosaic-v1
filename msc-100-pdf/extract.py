import fitz  # PyMuPDF
import re

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def structure_menu_data(menu_text):
    sections = re.split(r'\n(?=[A-Z][a-z]+s\n)', menu_text)
    menu = {}
    for section in sections:
        lines = section.strip().split('\n')
        category = lines[0]
        items = lines[1:]
        menu[category] = []
        for item in items:
            parts = item.split(' - ')
            if len(parts) == 2:
                name, price = parts
                menu[category].append({'name': name, 'price': price})
    return menu
