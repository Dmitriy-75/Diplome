import json
import requests
from requests import post
import time


headers = {'Authorization': 'Bearer example-auth-code'}

# payload = {
#     "firstname": "dmitri",
#     "lastname": "kas",
#     "email": "kasla@example.com",
#     "age": 49,
#     "job": "programmer"
# }
payload = {"firstname": "Anya",
           "lastname": "Ponomarev",
           "email": "anya@example.com",
           "age": 23,
           "job": "worker"}




start_time = time.time()
response = requests.request('POST',  "http://127.0.0.1:5000/users", headers=headers, json=payload)
duration = time.time() - start_time

print(f"Время исполнения   - {duration:.3f} sec")
print(response, response.json())



