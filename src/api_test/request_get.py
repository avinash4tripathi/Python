import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

resonse = requests.get(url)

print(resonse.status_code)
print(resonse.json())
print(resonse.text)