from flask import Flask, request, jsonify
import mysql.connector as ms
import requests
import json

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/masterServer', methods=['GET', 'POST'])
def get_data_servers():
    content = request.json

    info = json.dumps(content)
    print(info)

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    res = requests.post('http://localhost:5002/espanha', data=info, headers=headers)

    print(res.text.__contains__("null"))

    if res.text == 'null\n':

        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        res = requests.post('http://localhost:5001/portugal', data=info, headers=headers)

        return res.text

    else:
        return res.text


app.run()
