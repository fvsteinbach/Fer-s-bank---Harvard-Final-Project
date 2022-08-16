from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


@app.route("/")
def index():
  return render_template("index.html")


@app.route("/account", methods=["POST"])
def account():
  name = request.form.get("name")
  return render_template("account.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
