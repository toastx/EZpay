import json
from flask import request,Flask,render_template

app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template("home.html")




