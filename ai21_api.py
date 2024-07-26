# ai21_api.py
import requests
from config import AI21_API_KEY, AI21_API_URL

def get_ai21_response(message_text):
    headers = {
        "Authorization": f"Bearer {AI21_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "numResults": 1,
        "temperature": 0.7,
        "messages": [
            {"role": "user", "text": message_text}
        ],
        "system": "You are an AI assistant for business research. Your responses should be informative and concise."
    }

    response = requests.post(AI21_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        response_json = response.json()
        print(response_json)  # Agrega esta línea para ver la estructura de la respuesta
        if 'outputs' in response_json:
            return response_json['outputs'][0]['text'].strip()
        else:
            print("Unexpected response structure:", response_json)
            return None
    else:
        print(f"Response status code: {response.status_code}")
        print(f"Response text: {response.text}")
        return None
