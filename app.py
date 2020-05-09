from flask import Flask, render_template

app = Flask(__name__)

# Web page paths
@app.route("/")
def index():
    return render_template("logIn.html")

if __name__ == "__main__":
    app.run(debug=True)