import json
import requests
import time


headers = {'Authorization': 'Bearer example-auth-code'}

start_time = time.time()
response = requests.get("http://127.0.0.1:5000/users/1", headers=headers)
duration = time.time() - start_time

print(f"Время запроса   - {duration:.3f} sec")
print(response, response.json())






