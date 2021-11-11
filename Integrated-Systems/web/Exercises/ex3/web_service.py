import flask

app = flask.Flask(__name__)
app.config['DEBUG'] = True

enc_code = {}

@app.route('/lista_de_compras/', methods =['GET', 'POST'])

def get_request():
    content = flask.request.json

    for key in content:
        if key not in enc_code:
            enc_code[key] = content[key]
        else:
            enc_code[key] += content[key]

    print(enc_code)
    return flask.jsonify(enc_code)


app.run()
