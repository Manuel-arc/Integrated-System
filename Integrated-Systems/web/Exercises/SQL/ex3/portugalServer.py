from flask import Flask, request, jsonify
import mysql.connector as ms


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/portugal', methods=['get', 'post'])
def get_data_servers():
    content = request.json
    print(content['Nome'])
    mydb = ms.connect(
        host='localhost',
        user='root',
        password='root',
        database='Portugal'
    )

    mycursor = mydb.cursor()
    mycursor.execute("Select nome From Hotel where nome=\""+str(content['Nome'])+"\";")

    myresult = mycursor.fetchone()
    print(myresult)
    return jsonify(myresult)

app.run(port=5001)
