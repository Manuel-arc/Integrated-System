import flask

app = flask.Flask(__name__)
app.config['DEBUG'] = True

dic = {}

@app.route('/lista_de_compras/', methods =['GET', 'POST'])

def get_request():
    soma = 0
    content = flask.request.json

    for key in content:
        dic[key] = content[key]

    for i in dic:
        soma += dic[i]

    print(soma)

    return flask.jsonify(soma)


app.run()
