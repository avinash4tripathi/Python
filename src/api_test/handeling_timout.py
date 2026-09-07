import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

try:
    response = requests.get(url, timeout=5)

    if response.requests.status_code == 200:
      print("Request done")
    elif response.status_code == 404:
      print("user not found")
    elif response.status_code >= 500:
      print("serevr error")
    else:
      print("Request returned: ",response.status_code)

except requests.exceptions.Timeout:
 print("Request time out")

except requests.exceptions.RequestException as e:
 print("Request faild : ", e)