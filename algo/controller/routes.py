from flask import render_template, request, make_response, session, escape, url_for, redirect
from app import app
from model.user_info import UserInfo

@app.route("/")
def index():
    return render_template("logIn.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = UserInfo.get_by_email(request.form["username"])
        if user is not None and user.check_password(request.form["password"]):
            session["username"] = user.username
            return redirect(url_for("home"))

@app.route("/home")
def home():
    if "username" in session:
        return "Tu eres {}".format(escape(session["username"]))
    return "Debes de iniciar sesión primero"
