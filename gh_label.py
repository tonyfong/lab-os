import urllib.request
import json

with open('/home/agentuser/.gh_token', 'r') as f:
    token = f.read().strip()

# First, create the label if it doesn't exist
label_url = 'https://api.github.com/repos/tonyfong/lab-os/labels'
label_data = json.dumps({'name': 'hermes-done', 'color': '36adef'}).encode()
label_req = urllib.request.Request(label_url, data=label_data, headers={'Authorization': 'token ' + token, 'Content-Type': 'application/json'}, method='POST')
try:
    label_resp = urllib.request.urlopen(label_req)
    print('Label created:', label_resp.read().decode())
except urllib.error.HTTPError as e:
    if e.code == 422:  # Already exists
        print('Label already exists')
    else:
        print('Error creating label:', e.read().decode())

# Add label to issue
issue_url = 'https://api.github.com/repos/tonyfong/lab-os/issues/5/labels'
label_payload = json.dumps(['hermes-done']).encode()
issue_req = urllib.request.Request(issue_url, data=label_payload, headers={'Authorization': 'token ' + token, 'Content-Type': 'application/json'}, method='POST')
issue_resp = urllib.request.urlopen(issue_req)
print('Label added to issue:', issue_resp.read().decode())