import requests

response = requests.post("http://localhost:8080", data="35\n")
print(response.status_code)