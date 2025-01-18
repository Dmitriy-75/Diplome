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
# payload = {"firstname": "Anya",
#            "lastname": "Ponomarev",
#            "email": "anya@example.com",
#            "age": 23,
#            "job": "worker"}

# payload = {
#     "firstname": "kolya",
#     "lastname": "kas",
#     "email": "kola@example.com",
#     "age": 19,
#     "job": "worker"
# }
payload = {
    "firstname": "bom",
    "lastname": "kas",
    "email": "bom@example.com",
    "age": 24,
    "job": "programmer"
}




start_time = time.time()
response = requests.request('POST',  "http://127.0.0.1:8000/user/create_user", headers=headers, json=payload)
duration = time.time() - start_time

print(f"Время исполнения   - {duration:.3f} sec")
print(response, response.json())




