from flask import Flask, render_template, request
from pymysql import connections
import os
import boto3
from botocore.exceptions import ClientError
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
s3=boto3.client('s3')

#if call / then will redirect to that pg

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('Home.html')

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('StudRegister.html')


@app.route("/studentReg", methods=['GET','POST'])
def studentReg():
    cohort = request.form['cohort']
    intern_period = request.form['intern_period']
    student_name = request.form['student_name']
    student_id = request.form['student_id']
    student_ic = request.form['student_ic']
    gender = request.form['gender']
    programme = request.form['programme']
    student_email = request.form['student_email']
    student_contact = request.form['student_contact']
    uni_supervisor_name = request.form['uni_supervisor_name']
    uni_supervisor_email = request.form['uni_supervisor_email']

    insert_sql = "INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )"
    cursor = db_conn.cursor()

     

    try:

        cursor.execute(insert_sql, (cohort,intern_period,student_name,student_id,student_ic,gender,programme,student_email,student_contact,uni_supervisor_name,uni_supervisor_email))
        db_conn.commit()


        

    except Exception as e:
        return str(e) 
        

    finally:
        cursor.close()

    print("all modification done...")
    return render_template('StudRegister.html', registerSuccessful=True)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
