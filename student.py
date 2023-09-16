from flask import Flask, render_template, request
from pymysql import connections
import os
import boto3
from config import *

app = Flask(__name__)

bucket = custombucket
region = customregion


db_conn = connections.Connection(
    host=customhost,
    port=3306,
    user=customuser,
    password=custompass,
    db=customdb

)
output = {}
table = 'student'


#if call / then will redirect to that pg

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('StudRegister.html')


@app.route("/about", methods=['POST'])
def about():
    return render_template('Login.html') 


@app.route("/studentReg", methods=['POST'])
def studentReg():
    student_level = request.form['student_level']
    cohort = request.form['cohort']
    programme = request.form['programme']
    tutorial_group = request.form['tutorial_group']
    student_id = request.form['student_id']
    student_email = request.form['student_email']
    CGPA = request.form['cgpa']
    uni_supervisor_name = request.form['uni_supervisor_name']
    uni_supervisor_email = request.form['uni_supervisor_email']

    technical_knowledge = request.form['technical_knowledge']
    database_knowledge = request.form['database_knowledge']
    network_knowledge = request.form['network_knowledge']
   
    insert_sql = "INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s |)"
    cursor = db_conn.cursor()

     

    try:

        cursor.execute(insert_sql, (student_level,cohort,programme,tutorial_group,student_id,student_email,CGPA,uni_supervisor_name,uni_supervisor_email))
        db_conn.commit()
        

    except Exception as e:
        return str(e) 
        

    finally:
        cursor.close()

    print("all modification done...")
    return render_template('StudLogin.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
