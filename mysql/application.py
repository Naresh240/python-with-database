from flask import Flask, render_template,request
import mysql.connector

app= Flask(__name__)

mysql=mysql.connector.connect(database='vamsitestdb', user='admin', password='admin123', host='mysqldb.c79sd2kyheg7.us-east-1.rds.amazonaws.com')

@app.route('/',methods=['GET','POST'])

def index():
    cur=mysql.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Userdetail(firstname VARCHAR(20),lastname VARCHAR(20))")	
    mysql.commit()
 			
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        cur1=mysql.cursor()
        cur1.execute("INSERT INTO Userdetail(firstname, lastname) VALUES (%s, %s)", (firstName, lastName))
        mysql.commit()
        cur1.close()
        return 'success'
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
