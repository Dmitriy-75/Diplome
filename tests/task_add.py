import json
import requests
import time

url = "http://127.0.0.1:5000/"
headers = {'Authorization': 'Bearer example-auth-code'}


payload = {
    "title": "sleep",
    "content": "to t sleep",
    "priority": 2,
    "completed": False,
    "user_id": 4,
    "slug" : "eo"
}

# payload = {
#     "title": "work",
#     "content": "to  work",
#     "priority": 1,
#     "completed": False,
#     "user_id": 4,
#     "slug" : "eo"
# }

# payload = {
#     "title": "eat",
#     "content": "to eat",
#     "priority": 2,
#     "completed": False,
#     "user_id": 4,
#     "slug" : "eo"
# }
start_time = time.time()
# response = requests.request("POST", url+'/tasks', headers=headers, json=payload)
response = requests.request("POST","http://127.0.0.1:5000/tasks", headers=headers, json=payload)
duration = time.time() - start_time

print(f"Время запроса   - {duration:.3f} sec")
print(response, response.json())


