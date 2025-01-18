import json
import requests
import time

url = "http://127.0.0.1:8000/"
headers = {'Authorization': 'Bearer example-auth-code'}




payload = {
    "title": "lern",
    "content": "to  lern",
    "priority": 2,
    "completed": False,

    }

# payload = {
#     "title": "eat",
#     "content": "to eat",
#     "priority": 2,
#     "completed": False,

#
#     }

start_time = time.time()
# response = requests.request("POST", url+'/tasks', headers=headers, json=payload)
response = requests.request("POST","http://127.0.0.1:8000/task/create?user_id=3", headers=headers, json=payload)
duration = time.time() - start_time

print(f"Время запроса   - {duration:.3f} sec")
print(response, response.json())



