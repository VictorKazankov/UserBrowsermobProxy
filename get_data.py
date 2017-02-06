import requests
resp = requests.get('http://localhost:8080/proxy/8085/har')
resp.content
resp.json()