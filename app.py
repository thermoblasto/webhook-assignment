from flask import Flask, request, Response,json
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, Docker!'
  
@app.route('/webhook', methods=['POST'])

def respond():
    data = request.json
    idfv=data["idfv"]
    device_category=data["device_category"]
    advertising_id=data["advertising_id"]
    android_id=data["android_id"]
    af_sub1=data["af_sub1"]
    customer_user_id=data["customer_user_id"]
    is_lat=data["is_lat"]

    mydb = mysql.connector.connect(
       host="mysqldb",
       user="root",
       password="p@ssw0rd1",
       database="inventory"
     )
    cursor = mydb.cursor()
    cursor.execute(''' INSERT INTO attribution (idfv,device_category,af_sub1,customer_user_id,is_lat) VALUES(%s,%s,%s,%s,%s)''',(idfv,device_category,af_sub1,customer_user_id,is_lat))
    cursor.execute(''' INSERT INTO attribution_identifier (advertising_id,android_id) VALUES(%s,%s)''',(advertising_id,android_id))
    mydb.commit()
    cursor.close()
    return Response(status=200)