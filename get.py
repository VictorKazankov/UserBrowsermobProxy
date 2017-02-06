import requests
resp = requests.put('http://localhost:8080/proxy/8085/har', {"initialPageRef": "google"})