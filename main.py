
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

from urllib.parse import unquote

import json, db, AnimeApi, tioanime, MangaApi
import requests




app = Flask(__name__)
app.config.from_object(FlaskConfig)

ui = FlaskUI(app=app, width=768, height=800)

Anime=AnimeApi.AnimeFlv()
Anime.refresh_data()
Manga=MangaApi.LectorTMO()
Manga.get_populars()
completed= False
completedM = False

@app.route("/")
def main_page():
    return render_template("main.jinja",actual=db.get_theme_data())

@app.route("/Anime")
def anime_page():
    global Anime
    return render_template("anime.jinja",actual=db.get_theme_data(),data=Anime.act_data(),
                            refresh_A=True,searchA=True)

@app.route("/Anime/refresh")
def anime_refresh():
    global Anime
    Anime.refresh_data()
    return redirect(url_for('anime_page'))

@app.route("/Anime/search")
def anime_search():
    global Anime
    global completed
    completed = False
    try:
        change = request.args.get('search')
        Anime.search_Anime(change)
    except:
        return render_template("results.jinja",actual=db.get_theme_data(),
                                results=Anime.search["search"],searchA=True,
                                Favorites=db.get_favorites())
    return render_template("results.jinja",actual=db.get_theme_data(),
                            results=Anime.search["search"],searchA=True,
                            Favorites=db.get_favorites())


@app.route("/Watch/<path:path>")
def anime_video(path):
    f="/"+path
    global Anime
    Anime.get_recent_servers(f)
    
    AnimeInfo=Anime.Act_Ep
    
    xd = Anime.Act_servers
    
    return render_template("servers.jinja",actual=db.get_theme_data(),
                            Servers=xd, Anime=AnimeInfo )

@app.route("/Anime/Episodes/<path:path>")
def anime_eps(path):
    global Anime
    Anime.get_episodes(path)
    return render_template("anime_epi_list.jinja", actual=db.get_theme_data(),
                            DATA=Anime.Episodes)



@app.route("/Watch/ID/<path:idx>")
def watch_anime(idx):
    global Anime
    Anime.get_servers_id("/"+idx)
    return render_template("servers.jinja",actual=db.get_theme_data(), 
                            Servers=Anime.servers['servers'], Anime=Anime.servers )

@app.route("/Add/Favorites/<path:title>")
def save_anime(title):
    global Anime
    query=unquote(title)
    anime=Anime.search
    requested={}
    for results in anime['search']:
        if  results['title'] ==query:
            requested=results
            break
    db.add_favorites(requested['title'], requested['poster'])
    return render_template("results.jinja",actual=db.get_theme_data(),
                            results=Anime.search["search"],searchA=True,
                            Favorites=db.get_favorites())

@app.route("/Remove/Favorites/<path:title>")
def delete_anime(title):
    query=unquote(title)
    db.remove_favorites(query)
    if not completed:
        return render_template("results.jinja",actual=db.get_theme_data(),
                                results=Anime.search["search"],searchA=True,
                                Favorites=db.get_favorites())
    else:
        return render_template("results.jinja",actual=db.get_theme_data(),
                                results=db.get_favorites_full_data(),searchA=True,
                                Favorites=db.get_favorites())

@app.route("/Anime/Favorites")
def favorite_animes():
    global completed
    completed = True
    return render_template("results.jinja",actual=db.get_theme_data(),
                            results=db.get_favorites_full_data(),searchA=True,
                            Favorites=db.get_favorites())

    
@app.route("/Manga")
def manga_page():
    global Manga
    return render_template("manga.jinja",actual=db.get_theme_data(),
                            Data= Manga.populars, searchM=True )

@app.route("/Manga/ReadList/<path:url>")
def manga_episodes(url):
    global Manga
    url=unquote(url)
    Manga.get_episodes(url)
    
    return render_template("manga_epi_list.jinja", chapters=Manga.Episodes, 
                            actual=db.get_theme_data())

@app.route("/Manga/Read/<path:url>")
def read_chapter(url):
    global Manga
    Manga.get_chapter_info(url)

    return render_template("cascade.jinja", images=Manga.pictures,
                            actual=db.get_theme_data())

@app.route("/Manga/Search")
def manga_search():
    global Manga
    global completedM
    completedM = False
    data= [{'link': None, 'img': [], 'title': None, 'genre': None}]
    try:
        change = request.args.get('search')
        Manga.make_search(unquote(change))
        print(unquote(change))
        print(Manga.search)
    except:
        return render_template("manga_results.jinja",actual=db.get_theme_data(),
                                results=Manga.search,searchM=True, data=data
                                )
    return render_template("manga_results.jinja",actual=db.get_theme_data(),
                            results=Manga.search,searchM=True, data=data
                            )



@app.route("/Config")
def config_page():
    return render_template("Config.jinja", themes=Config.theme,  
                            theme=db.get_theme(), actual=db.get_theme_data())

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
#ui.run()