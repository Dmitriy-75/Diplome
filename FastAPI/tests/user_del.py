import json
import requests
import time


headers = {'Authorization': 'Bearer example-auth-code'}

start_time = time.time()
response = requests.request('DELETE',  "http://127.0.0.1:8000/user/del_user/2", headers=headers)
duration = time.time() - start_time

print(f"Время исполнения   - {duration:.3f} sec")
print(response, response.text)