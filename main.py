
from flask import (
    Flask,
    render_template,
    send_from_directory,
    request,
    g,
    session,
    redirect,
    url_for,
    flash
)
from flaskwebgui import FlaskUI

from config_file import FlaskConfig


app = Flask(__name__, template_folder="Templates")
app.config.from_object(FlaskConfig)

ui = FlaskUI(app=app, width=768, height=800)

@app.route("/")
def main_page():
    return render_template("main.jinja")

@app.route("/Anime")
def anime_page():
    return render_template("anime.jinja")

@app.route("/Manga")
def manga_page():
    return render_template("manga.jinja")


app.run(debug=True)