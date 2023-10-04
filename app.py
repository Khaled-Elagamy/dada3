import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd
from pymongo import MongoClient

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)


# Configure CS50 Library to use SQLite database
#db = SQL("sqlite:///student.db")
client = MongoClient(os.getenv("DATA_URL"))
db = client['student']

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

users_collection = db['users']

class User:
    def __init__(self, username, house):
        self.username = username
        self.house = house



@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():

    return render_template("index.html")

@app.route("/option1")
@login_required
def option1():

    return render_template("option1.html")

@app.route("/option2")
@login_required
def option2():

    return render_template("option2.html")
@app.route("/option3")
@login_required
def option3():

    return render_template("option3.html")


@app.route("/thehut")
@login_required
def thehut():
    return render_template("thehut.html")


@app.route("/end")
@login_required
def end():
    return render_template("end.html")

@app.route("/face")
@login_required
def face():
    return render_template("face.html")

@app.route("/theclue", methods=["GET", "POST"])
@login_required
def theclue():
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("answer"):
            return apology("insert answer", 403)

    true = "alohomora"
    answer = request.form.get("answer")

    if true == answer:
        return render_template("thehut.html")
    else:
        return apology("wrong answer", 403)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide the student name", 403)

        # Ensure password was submitted
        elif not request.form.get("house"):
            return apology("choose your house", 403)

        # Create a new user document and insert it into the MongoDB collection
        new_user = User(request.form.get("username"), request.form.get("house"))
        users_collection.insert_one(new_user.__dict__)

        # Ensure username exists and password is correct
        #if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            #return apology("invalid username and/or password", 403)
        

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")
