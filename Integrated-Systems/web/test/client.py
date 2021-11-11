import requests
import xmltodict

my_list = {
    'mytext': 'lalala'
}

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

res = requests.post('http://localhost:5000/lista_de_compras/123', data = xmltodict.unparse(my_list), headers=headers)

if res.ok:
    print(res.json())
    print('Pedido feito')


