import requests
import json

mydict={
    "Citizen": {
        "Name": 'Manuel'
    }
}

headers = headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

res = requests.post('http://localhost:5000/getname', data = json.dumps(mydict), headers=headers)

if res.ok:
    print(res.json())
