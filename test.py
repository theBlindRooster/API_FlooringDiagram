import mysql.connector
import json
import datetime

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="KTpfd!@21",
  database="pfd"
)
output=[]
cursor = mydb.cursor(dictionary=True)
cursor.execute("SELECT * FROM planflooringdiagramcoords")

for row in cursor:
    output.append(row)
print(output)
