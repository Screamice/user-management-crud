from flask import Flask
from controller.connection import Connection

# Flask configurations
app = Flask(__name__)

app.secret_key = "12345"

database = Connection()
app.config["SQLALCHEMY_DATABASE_URI"] = database.get_connection()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
DB = database.enable_connection(app)

if __name__ == "__main__":
    app.run(debug=True)