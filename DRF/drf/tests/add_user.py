import time
import json
import requests
from requests import post

headers = {'Authorization': 'Bearer example-auth-code'}

payload = {
    "firstname": "Liya",
    "lastname": "Kas",
    "email": "lilya@example.com",
    "age": 42,
    "job": "worker"
}

start_time = time.time()
response = requests.request('POST', "http://127.0.0.1:8000/api/user_class", headers=headers, json=payload)
duration = time.time() - start_time

print(f"Время исполнения   - {duration:.3f} sec")
print(response, response.json())
