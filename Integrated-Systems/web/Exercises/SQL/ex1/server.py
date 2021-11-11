from flask import Flask, request, Response, jsonify
import mysql.connector

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/getname', methods=['GET', 'POST'])
def verify_product():
    content = request.json
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Integration"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM teste;")

    myresult = mycursor.fetchall()

    return jsonify(myresult)

app.run()
