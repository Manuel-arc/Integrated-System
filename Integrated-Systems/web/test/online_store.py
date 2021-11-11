from flask import Flask, request, jsonify
import xmltodict

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/lista_de_compras/<numero>', methods =['GET', 'POST'])

def get_request(numero):
    content = xmltodict.parse(request.data)
    print(content['mytext'])
    return jsonify({'uuid': numero})


app.run()
