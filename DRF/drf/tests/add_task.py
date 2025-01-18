import json
import requests
import time

url = "http://127.0.0.1:8000/"
headers = {'Authorization': 'Bearer example-auth-code'}


payload = {
    "title": "Task 2",
    "content": "to drink cofee",
    "priority": 2,
    "completed": True,
    "user_id": 4,
}

start_time = time.time()
response = requests.request("POST", url+'/api'+'/task_class', headers=headers, json=payload)
duration = time.time() - start_time

print(f"Время исполнения   - {duration:.3f} sec")
print(response, response.json())


