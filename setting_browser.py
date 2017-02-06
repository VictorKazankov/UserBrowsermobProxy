import requests
resp = requests.post('http://localhost:8085/proxy', {})
print resp
print resp.content

port = resp.json()['port']
print port

