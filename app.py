from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """Render a page with dynamic data from Python."""
    items = ["Apple", "Banana", "Orange"]
    return render_template(
        "index.html",
        username="Darshan",
        date=datetime.now().strftime("%Y-%m-%d"),
        items=items,
    )


@app.route("/about")
def about():
    """Render the About page using the shared base template."""
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
