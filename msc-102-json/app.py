from flask import Flask, request, jsonify
from menu import read_menu_from_json
from chatbot import process_user_query

app = Flask(__name__)

# Load the menu from JSON file
json_path = "offers.json"
menu = read_menu_from_json(json_path)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = process_user_query(user_input, menu)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
