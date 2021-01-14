from flask import Flask, render_template, request
import psycopg2

app=Flask(__name__)

postgresdb = psycopg2.connect(database="postgres", user="postgres", password="Naresh#240", host="localhost", port="5432")
postgrescur = postgresdb.cursor()

@app.route('/insertemployee', methods=['POST', 'GET'])

def insertemployee():
    postgrescur.execute("CREATE TABLE IF NOT EXISTS employee(empno VARCHAR(20),empname VARCHAR(20),salary VARCHAR(20))")	
    postgresdb.commit()
 			
    if request.method == "POST":
        details = request.form
        empno = details['empno']
        empname = details['empname']
        salary  = details['salary']
        postgrescur.execute("INSERT INTO employee(empno, empname, salary) VALUES (%s, %s, %s)", (empno, empname, salary))
        postgresdb.commit()
        return 'Employee successfullly created'
    return render_template('insertemployee.html')

@app.route('/listofemployees', methods=['GET'])
def listofemployees():
    if request.method == "GET":
        postgrescur.execute("select * from employee")
        result = postgrescur.fetchall()
        return render_template('listofemployees.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)