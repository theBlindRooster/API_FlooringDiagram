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
  passwd="",
  database="pfd"
)
#################################################
# Routes
#################################################

@app.route("/api/diagram", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        # nickname = request.form["nickname"]
        # age = request.form["age"]

        # pet = Pet(nickname=nickname, age=age)
        # db.session.add(pet)
        # db.session.commit()

        return "Thanks for the form data!"

    output=[]
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM planflooringdiagramcoords")

    for row in cursor:
        output.append(row)
    return jsonify(output)

@app.route("/")
def home():
    return "Welcome!"

if __name__ == "__main__":
    app.run()
