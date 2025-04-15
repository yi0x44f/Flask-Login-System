import requests
import json
import os
from dotenv import load_dotenv
load_dotenv(override=True)  # Load environment variables from .env file




response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer " + os.getenv("OPENROUTER_API_KEY"), # Replace with your OpenRouter API key
    "Content-Type": "application/json",
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  data=json.dumps({
    "model": "deepseek/deepseek-chat-v3-0324:free",
    "messages": [
      {
        "role": "user",
        "content": "What is the meaning of life?"
      }
    ],
    
  })
)
print(response.status_code)
print(response.json())
