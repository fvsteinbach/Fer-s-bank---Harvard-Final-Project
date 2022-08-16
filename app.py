from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
  return render_template("index.html")


@app.route("/create-account.html", methods=["POST","GET"])
def account():
    return render_template("create-account.html")

#@app.route("/create-account", methods=["POST"])
#def create_account():
#  name=request.form.get("name")
#  account_balance=request.form.get("balance")
#  return render_template("create-account.html", name=name, #account_balance=account_balance)

if __name__ == "__main__":
    app.run(debug=True)
