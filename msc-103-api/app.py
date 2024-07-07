from flask import Flask, request, jsonify
from api import get_offers
from chatbot import process_user_query

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    menu = get_offers()
    response = process_user_query(user_input, menu)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
