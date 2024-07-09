import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


def process_user_query(query, menu):
    prompt = f"Menu: {menu}\n\nUser: {query}\nAI:"
    response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=50)
    return response.choices[0].text.strip()
