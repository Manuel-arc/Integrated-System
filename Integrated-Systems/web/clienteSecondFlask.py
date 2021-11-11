import requests
import json

mydict = {
    'mytext':'lalala'
}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}


res = requests.post('http://localhost:5000/api/add_message/1234', data=json.dumps(mydict), headers=headers)

if res.ok:
    print(res.json())
