import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def format_menu_for_prompt(menu):
    formatted_menu = ""
    for category, items in menu.items():
        formatted_menu += f"{category}:\n"
        for item in items:
            formatted_menu += f"- {item['name']} ({item['price']}): {item['description']}\n"
    return formatted_menu

def process_user_query(query, menu):
    menu_prompt = format_menu_for_prompt(menu)
    prompt = f"Menu:\n{menu_prompt}\n\nUser: {query}\nAI:"
    
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    
    # return response['choices'][0]['message']['content'].strip()
    return response
