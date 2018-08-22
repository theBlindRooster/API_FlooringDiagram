# import necessary libraries
import numpy as np
from flask import (
    Flask,
    render_template,
    jsonify,
    request)

import mysql.connector
import json
import datetime

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Database Setup
#################################################
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=,
  database="pfd"
)
#################################################
# Routes
#################################################

@app.route("/api/diagram", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        coords=request.form['coords']
        areaid=request.form['areaid']
        return "coordinates= "+str(coords)+" id="+str(areaid)

    rooms=[]
    diagram=[]
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM planflooringdiagramcoords WHERE communityid = "+str(request.args.get('cid'))+" AND planid = "+str(request.args.get('pid')))

    for row in cursor:
        rooms.append(row)
    
    cursor.execute("SELECT * FROM planflooringdiagram WHERE planid = "+str(request.args.get('pid')))

    for row in cursor:
        diagram.append(row)
   
    output={'rooms':rooms,'diag':diagram}
    return jsonify(output)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/diagram")
def diagram():
    return render_template('diagramconfig.html')

if __name__ == "__main__":
    app.run()
