from flask import Flask, render_template, request, redirect
import sqlite3


app = Flask(__name__)
account_list = {}


@app.route("/", methods=["POST", "GET"])
def index():
  return render_template("index.html")


@app.route("/add-account.html")
def add_account():
    return render_template("add-account.html")


@app.route("/create-account.html")
def create_account():
    #Validade name
    account_owner = request.form.get("fname" + " " + "lname")
    if not account_owner:
      return render_template("error.html", message="Missing name")

    #Validate account_balance
    account_balance = request.form.get("balance")
    if not account_balance:
       return render_template("error.html", message="Missing balance")
    


@app.route("/remove-account.html")
def remove_account():
  return render_template("remove-account.html")


@app.route("/see-account.html")
def see_account():
  return render_template("see-account.html")


@app.route("/operation.html")
def operation():
  return render_template("operation.html")


@app.route("/reports.html")
def reports():
  return render_template("reports.html")


app.run(debug=True)
