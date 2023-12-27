import requests
import json

url = "http://localhost:11434/api/generate"

data = {
    "model": "mistral:7b",
    "prompt": "Using less than 10 words, tell me what color is the sky."
}

response = requests.post(url, json=data)

data = response.text.splitlines()
response_list = [json.loads(line)['response'] for line in data]
print(''.join(response_list))
