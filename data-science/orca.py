import requests
import json

url = "http://localhost:11434/api/generate"

data = {
    "model": "orca-mini:3b",
    "system": "Always answer using ten or less words.",
    "prompt": "Tell me why the sky is blue."
}

response = requests.post(url, json=data)
data = response.text.splitlines()
response_list = [json.loads(line)['response'] for line in data]

print(''.join(response_list))
