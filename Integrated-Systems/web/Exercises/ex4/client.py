import requests
import json

my_list = {
    "joao": 10,
    "armindo": 20,
    "jose": 15
}

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

res = requests.post('http://localhost:5000/lista_de_compras/', data = json.dumps(my_list), headers=headers)

if res.ok:
    print(res.text)
    print('Pedido feito')


