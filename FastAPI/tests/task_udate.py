import json
import requests
import time

url = "http://127.0.0.1:8000/"
headers = {'Authorization': 'Bearer example-auth-code'}


payload = {
    "title": "see",
    "content": "to see",
    'priority':1,
    'completed':True,
    "user_id": 4,
}

# payload = {
#     "title": "program",
#     "content": "to programming better",
#     "priority": 1,
#     "completed": False,
#     "user_id": 4,
# }


start_time = time.time()
response = requests.request("PUT", url+'/task'+'/update?task_id=2', headers=headers, json=payload)
duration = time.time() - start_time

print(f"Время исполнения   - {duration:.3f} sec")
print(response, response.json())

