import flask

app = flask.Flask(__name__)
app.config['DEBUG'] = True

dic = []

@app.route('/lista_de_compras/<numero>', methods =['GET', 'POST'])

def get_request(numero):
    content = flask.request.json
    dic.append(content)
    print("{} => {}".format(numero, content))
    print(dic)
    return 'ok'


app.run()
