import requests
import json

mylist = {
    "Nome": "Porto Hotel"
}

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

res = requests.post('http://localhost:5000/masterServer', data=json.dumps(mylist), headers=headers)

if res.ok:
    if res.text == {}:
        print("aaaaa")
    else:
        print(res.json())
