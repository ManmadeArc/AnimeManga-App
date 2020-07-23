from pyquery import PyQuery as pq
import requests, js2py, json, urllib.parse
site="https://tioanime.com"




def get_latest_episodes():
    doc = pq(site, parser = 'html')

    animes=doc.find('#tioanime > div > section:nth-child(2) > ul > li')
    episodes={}
    episodes['episodes']=[]
    for event in animes.items():
        article={}  
        article['title']=event.find('article > a > h3').text()
        article['poster']=site + event.find('article > a > div > figure > img').attr("src")
        article['id']=event.find('article > a').attr("href")
        article['servers']=get_servers(article['id'])
        episodes['episodes'].append(article)
    return episodes

        

def get_servers(link, dicti=False):
    doc= pq(site+link, parser = 'html')
    query=doc.find("body > script:nth-child(21)")
    Data=_servers_from_script(query)
    servers=[]
    for server in Data:
        info={}
        info['title']=server[0]
        info['code']=server[1]
        servers.append(info)
    if dicti:
        anime={}
        anime['servers']=servers
        return anime
    else:
        return servers



def _servers_from_script(script):
    jsExpression=list(script.text())
    for _ in range(51):
        jsExpression.pop(-1)
    jsExpression="".join(jsExpression)
    jsExpression= "function my_function(){" + jsExpression +"return videos; };"
    get_emmbed= js2py.eval_js(jsExpression)

    return list(get_emmbed())


def search(query):
    search=urllib.parse.quote_plus(query)
    link = site+"/directorio?q="+ search
    doc = pq(link, parser = 'html')
    results=doc.find("#tioanime > div > div.row.justify-content-between.filters-cont > main > ul > li")
    lista=[]
    searches={}
    
    for event in results.items():
        article={}
        article['title']=event.find('article > a > h3').text()
        article['poster']=site + event.find('article > a > div > figure > img').attr("src")
        article['id']=event.find('article > a').attr("href")
        article['synopsis'], article['episodes']=get_aditional_info(article['id'])
        lista.append(article)
    searches["search"]=lista
    return searches


def _get_episodeList_from_Script(script):
    jsExpression=list(script.text())
    for _ in range(51):
        jsExpression.pop(-1)
    jsExpression="".join(jsExpression)

    jsExpression1= "function my_function(){" + jsExpression +" ; return anime_info; };"
    jsExpression2="function my_function(){" + jsExpression +" ; return episodes; };"
    get_anime_info= js2py.eval_js(jsExpression1)
    get_episodes= js2py.eval_js(jsExpression2)

    anime_info=get_anime_info()
    episodes=get_episodes()
    result=[]
    for i in episodes:
        lista={}
        lista['episode']=i
        lista['id']="/ver/"+anime_info[1]+"-"+str(i)
        result.append(lista)
    return result



def get_aditional_info(link, poster=False):
    doc=pq(site+link, parser = 'html')
    sinopsis=doc.find("#tioanime > article > div > div > aside.col.col-sm-8.col-lg-9.col-xl-10 > p.sinopsis").text()
    
    script=doc.find('body > script:nth-child(21)')
    episodes=_get_episodeList_from_Script(script)
    if poster:
        poster=doc.find('#tioanime > article > div > div > aside.col.col-sm-4.col-lg-3.col-xl-2 > div > figure > img').attr('src')
        return sinopsis, poster ,episodes
    else:
        return sinopsis, episodes
