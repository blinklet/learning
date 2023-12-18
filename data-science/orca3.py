import requests
import json

url = "http://localhost:11434/api/generate"

data1 = {
    "model": "orca-mini:3b",
    "prompt": "Talk like a prirate when answering all future questions."
}

response = requests.post(url, json=data1)


data = {
    "model": "orca-mini:3b",
    "prompt": "Why do we drive on the right side of the road?"
}

response = requests.post(url, json=data)


data = response.text.splitlines()
response_list = [json.loads(line)['response'] for line in data]

print(''.join(response_list))
