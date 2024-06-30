from flask import Flask, request, jsonify
from menu import read_menu_from_csv
from chatbot import process_user_query

app = Flask(__name__)

# Load the menu from CSV file
csv_path = "menu.csv"
menu = read_menu_from_csv(csv_path)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = process_user_query(user_input, menu)
    # return jsonify({'user input': user_input})
    # return jsonify({'menu': menu})
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)