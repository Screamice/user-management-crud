from flask import Flask, render_template, request, make_response, session, escape, url_for, redirect
from controller.connection import Connection

# Flask configurations
app = Flask(__name__)

app.secret_key = "12345"

database = Connection()
app.config["SQLALCHEMY_DATABASE_URI"] = database.get_connection()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
DB = database.enable_connection(app)

# Web page paths
@app.route("/")
def index():
    return render_template("logIn.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        pass



if __name__ == "__main__":
    app.run(debug=True)