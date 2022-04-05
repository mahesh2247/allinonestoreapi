import requests
import json

url = "http://127.0.0.1:5000/processjson"

payload = json.dumps([
  {
    "item": "Headache pills",
    "itemCategory": "Medicine",
    "quantity": 5,
    "price": 50
  },
  {
    "item": "Sandwich",
    "itemCategory": "Food",
    "quantity": 2,
    "price": 200
  },
  {
    "item": "Perfume",
    "itemCategory": "Imported",
    "quantity": 1,
    "price": 4000
  },
  {
    "item": "Black Swan",
    "itemCategory": "Book",
    "quantity": 1,
    "price": 300
  }
])
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)