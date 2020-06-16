
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

from config_file import (FlaskConfig, Config)

import json, db, AnimeApi



app = Flask(__name__)
app.config.from_object(FlaskConfig)

ui = FlaskUI(app=app, width=768, height=800)

owo=AnimeApi.AnimeFlv()
owo.refresh_data()

@app.route("/")
def main_page():
    return render_template("main.jinja",actual=db.get_theme_data())

@app.route("/Anime")
def anime_page():
    global owo
    return render_template("anime.jinja",actual=db.get_theme_data(),data=owo.act_data(),refresh_A=True)

@app.route("/Anime/refresh")
def anime_refresh():
    global owo
    owo.refresh_data()
    return redirect(url_for('anime_page'))

@app.route("/Manga")
def manga_page():
    return render_template("manga.jinja",actual=db.get_theme_data() )

@app.route("/Config")
def config_page():
    return render_template("Config.jinja", themes=Config.theme, theme=db.get_theme(), actual=db.get_theme_data())

@app.route('/set', methods=['POST'])
def set_setting():
    change = request.form
    for key, val in change.items():
        is_defined = type(Config.__dict__.get(key, None)) == dict
        if is_defined:
            options = Config.__dict__[key]
            if val not in options:
                continue
            db.savetheme(val)
    
    return redirect(url_for('config_page'))


app.run(debug=True)