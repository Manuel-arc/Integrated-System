import requests
import xmltodict

class MyClass:

    def __init__(self):
        self.my_dict = {
            "words": {
                "amanha": 2,
                "depois": 4,
                "sim": 8
            }
        }


obj = MyClass()

headers = {'Content-type': 'application/xml', 'Accept': 'text/plain'}

res = requests.post("http://localhost:5000/api/add_dic", data=xmltodict.unparse(obj.my_dict), headers = headers)

if res.ok:
    print(res.json())
