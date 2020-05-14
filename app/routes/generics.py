from app import APP

@APP.route("/")
def index():
    return "Soy el index"