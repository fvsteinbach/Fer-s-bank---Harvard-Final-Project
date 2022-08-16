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


@app.route("/create-account.html", methods=["POST", "GET"])
def create_account():
    #Validade first name
    name = request.form.get("name")
    if not name:
      return render_template("error.html", message="Missing name")
    
    #Validate account_balance
    balance = request.form.get("balance")
    if not balance:
      return render_template("error.html", message="Missing balance")
    
    #Rember the balance 
    account_list[name] = balance

    #Confirm account creation
    return render_template("created.html")


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
