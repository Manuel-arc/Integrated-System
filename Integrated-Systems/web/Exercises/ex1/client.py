import requests
import json

my_list = ["Casaco", 'Camisola']

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

res = requests.post('http://localhost:5000/lista_de_compras/123', data = json.dumps(my_list), headers=headers)

if res.ok:
    print(res.text)
    print('Pedido feito')


