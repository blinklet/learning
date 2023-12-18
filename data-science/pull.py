import requests

url = "http://localhost:11434/api/pull"

data = {
    "name": "orca-mini:3b"
}

response = requests.post(url, json=data)
print(response.text)
