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
    return render_template('StudRegister.html')


@app.route("/studentReg", methods=['GET','POST'])
def studentReg():
    cohort = request.form['cohort']
    internPeriod = request.form['internPeriod']
    studName = request.form['studName']
    studId = request.form['studId']
    studIc = request.form['studIc']
    studGender = request.form['studGender']
    programme = request.form['programme']
    studEmail = request.form['studEmail']
    studContact = request.form['studContact']
    uniSupervisor = request.form['uniSupervisor']
    uniEmail = request.form['uniEmail']

    insert_sql = "INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )"
    cursor = db_conn.cursor()

     

    try:

        cursor.execute(insert_sql, (cohort,internPeriod,studName,studId,studIc,studGender,programme,studEmail,studContact,uniSupervisor,uniEmail))
        db_conn.commit()


        

    except Exception as e:
        return str(e) 
        

    finally:
        cursor.close()

    print("all modification done...")
    return render_template('StudRegister.html', registerSuccessful=True)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
