from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def index():
  return render_template("index.html")


@app.route("/account")
def account():
  name = request.args.get("name")
  return render_template("account.html", name=name)


if __name__ == "__main__":
    app.run()
