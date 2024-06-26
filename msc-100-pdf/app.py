from flask import Flask, request, jsonify
from extract import extract_text_from_pdf, structure_menu_data
from chatbot import process_user_query

app = Flask(__name__)

# Extract and structure the menu data once at the start
pdf_path = "menu.pdf"
menu_text = extract_text_from_pdf(pdf_path)
menu = structure_menu_data(menu_text)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = process_user_query(user_input, menu)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
