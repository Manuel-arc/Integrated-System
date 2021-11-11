import flask
import xmltodict

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/api/add_dic', methods = ['POST'])

def add_dic():
    content = xmltodict.parse(flask.request.data)
    print(content)

    return flask.jsonify(content)

app.run()
