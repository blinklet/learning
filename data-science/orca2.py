import requests

url = "http://localhost:11434/api/generate"

data = {
    "model": "orca-mini:3b",
    "prompt": "Using less than 10 words, tell me what color is the sky."
}

response = requests.post(url, json=data)
print(response.text)
