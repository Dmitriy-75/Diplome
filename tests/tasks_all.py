import json
import requests
import time

url = "http://127.0.0.1:5000/"
headers = {'Authorization': 'Bearer example-auth-code'}

start_time = time.time()
response = requests.get(url+'/tasks', headers=headers)
duration = time.time() - start_time

print(f"Время исполнения   - {duration:.3f} sec")
print(response, response.text)


