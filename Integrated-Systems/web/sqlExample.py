from flask import Flask, request, Response
import mysql.connector

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/getname', methods=['GET', 'POST'])
def update_data_json():
    content = request.json
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Integration"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM teste;")
    myresult = mycursor.fetchone()
    print(myresult)
    return Response(str(myresult), mimetype='text')

app.run()

