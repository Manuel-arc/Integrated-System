import requests
import xmltodict
import json

class MyClass:

    def __init__(self):
        self.my_dict = {
            "words": {
                "amanha": 2,
                "depois": 4,
                "sim": 8
            }
        }


    def update_stock(self, same, amanha):
        self.my_dict['words'][same] = amanha

    def add_stock(self):
        pass

    def to_xml(self):
        return xmltodict.unparse(self.my_dict)

    def to_json(self):
        return json.dumps(self.my_dict)

obj = MyClass()

headers = {'Content-type': 'application/xml', 'Accept': 'text/plain'}

res = requests.post("http://localhost:5000/api/add_dic", data=obj.to_xml(), headers = headers)

if res.ok:
    print(res.json())


obj.update_stock("nao", 4)

headers = {'Content-type': 'application/xml', 'Accept': 'text/plain'}

res = requests.post("http://localhost:5000/api/add_dic", data=obj.to_xml(), headers = headers)

if res.ok:
    print(res.json())


