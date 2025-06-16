import requests
import json
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

BASE_URL = "https://openrouter.ai/api/v1"
MODEL = "google/gemini-2.5-pro-preview:free"


OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY environment variable not set")

# Send request
response = requests.post(
    url=f"{BASE_URL}/chat/completions",
    headers={
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    },
    json={  # Use json= instead of data=json.dumps()
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": "What is the meaning of life?"
            }
        ]
    }
)


if response.status_code != 200:
    print("Error:", response.status_code, response.text)
    exit()


data = response.json()
try:
    content = data['choices'][0]['message']['content']
    print("AI Response:", content)
except (KeyError, IndexError) as e:
    print("Unexpected response format:", data)
