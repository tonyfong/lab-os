import urllib.request
import json

# Read token from file
with open('/home/agentuser/.gh_token', 'r') as f:
    token = f.read().strip()

url = 'https://api.github.com/repos/tonyfong/lab-os/issues/5/comments'
data = json.dumps({'body': 'Fixed the layout — form now properly arranges components for desktop/tablet view without overlaps. Please review. — Hermes Agent'}).encode()
req = urllib.request.Request(url, data=data, headers={'Authorization': 'token ' + token, 'Content-Type': 'application/json'})
resp = urllib.request.urlopen(req)
print(resp.read().decode())