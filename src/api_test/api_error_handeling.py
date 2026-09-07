import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

resonse = requests.get(url)

try:
     resonse = requests.get(url, timeout=5)

     if resonse.raise_for_status == 200:
            print("request sucesfull")
            print("response:",resonse.json())

     elif resonse.status_code == 404:
            print("user not found")

     elif resonse.status_code >= 500:
            print("Server error")
     else:
            print("request returned:",resonse.status_code)

except resonse.requestException as e:
       print("Request fail: d",e) # here e == error




