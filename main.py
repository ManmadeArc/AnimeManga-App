
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
    return render_template("anime.jinja",actual=db.get_theme_data(),data=owo.act_data(),refresh_A=True,searchA=True)

@app.route("/Anime/refresh")
def anime_refresh():
    global owo
    owo.refresh_data()
    return redirect(url_for('anime_page'))

@app.route("/Anime/search")
def anime_search():
    change = request.args.get('search')
    owo.search_Anime(change)
    return render_template("results.jinja",actual=db.get_theme_data(),results=owo.search["search"],searchA=True)


@app.route("/Watch/<path:path>")
def anime_video(path):
    f=path
    global owo
    owo.get_recent_servers(f)
    AnimeInfo=owo.Act_Ep
    xd = owo.Act_servers

    return render_template("servers.jinja",actual=db.get_theme_data(), Servers=xd, Anime=AnimeInfo )

@app.route("/Anime/Episodes/<path:path>")
def anime_eps(path):
    global owo
    owo.get_episodes(path)
    return render_template("anime_epi_list.jinja", actual=db.get_theme_data(), DATA=owo.Episodes)


@app.route("/Watch/ID/<path:idx>")
def watch_anime(idx):
    global owo
    owo.get_servers_id(idx)
    return render_template("servers.jinja",actual=db.get_theme_data(), Servers=owo.servers['servers'], Anime=owo.servers )



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



app.run(host='192.168.31.155')
#ui.run()