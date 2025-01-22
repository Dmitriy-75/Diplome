import json
import requests
import time


headers = {'Authorization': 'Bearer example-auth-code'}

start_time = time.time()
response = requests.get("http://127.0.0.1:8000/api/user_class/2", headers=headers)
duration = time.time() - start_time

print(f"Тест метода   - {duration:.3f} sec")
print(response, response.json())






