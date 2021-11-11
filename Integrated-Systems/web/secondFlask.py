from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/api/add_message/<uuid>', methods = ['GET', 'POST'])

def add_message(uuid):
    content = request.json

    print(content['mytext'])

    return jsonify({'uuid': uuid})

app.run()
