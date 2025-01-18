import json
import requests
import time

headers = {'Authorization': 'Bearer example-auth-code'}

# payload = {
#     "firstname": "Janna",
#     "lastname": "Из тех королев",
#     "email": "jana29@gmail.com",
#     "age": 33,
#     "job": "Queen"}

payload = {
    "firstname": "Janna",
    "lastname": "Из тех королев",
    }

start_time = time.time()
response = requests.request('PATCH',  "http://127.0.0.1:5000/users/1", json=payload, headers=headers)
duration = time.time() - start_time

print(f"Время исполнения   - {duration:.3f} sec")
print(response, response.json())





