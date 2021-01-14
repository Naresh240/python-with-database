from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

mysqldb = mysql.connector.connect(host='localhost',user='root',passwd='Naresh#240',database='mysql')
my_database=mysqldb.cursor()
my_database.execute("CREATE TABLE IF NOT EXISTS employee(empno VARCHAR(20) PRIMARY KEY,empname VARCHAR(20),salary VARCHAR(20))")
mysqldb.commit()

@app.route('/insertemployee', methods=['POST', 'GET'])
def insertemployee():
    if request.method == "POST":
        details = request.form
        empno = details['empno']
        empname = details['empname']
        salary = details['salary']
        my_database=mysqldb.cursor()
        my_database.execute("INSERT INTO employee(empno, empname, salary) VALUES (%s, %s, %s)", (empno, empname, salary))
        mysqldb.commit()
        my_database.close()
        return 'successfully employee created'
    return render_template('insertemployee.html')

@app.route('/listofemployees', methods=['GET'])
def listofemployees():
    if request.method == "GET":
        my_database=mysqldb.cursor()
        my_database.execute("select * from employee")
        result = my_database.fetchall()
        return render_template('listofemployees.html', result=result)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)