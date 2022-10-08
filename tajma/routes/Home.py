import routes

@routes.app.route("/", methods=["GET", "POST"])
def home():
    return routes.render_template("index.html")