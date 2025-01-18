import json
import requests
import time

headers = {'Authorization': 'Bearer example-auth-code'}

payload = {
    "firstname": "Janna",
    "lastname": "Из тех королев",
    "email": "jana29@gmail.com",
    "age": 33,
    "job": "Queen"}
#
# payload = {
#
#     "firstname": "Janna",
#     "lastname": "Из тех королев",
#     "email": "den@yandex.ru",
#     "age": 22,
#     "job":"ingeneer"
#     }

start_time = time.time()
response = requests.request('PUT',  "http://127.0.0.1:8000/user/update_user?user_id=2", json=payload, headers=headers)
duration = time.time() - start_time

print(f"Время исполнения   - {duration:.3f} sec")
print(response, response.json())





