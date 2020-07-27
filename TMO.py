from pyquery import PyQuery as pq
import requests, js2py, json, urllib.parse
import re


hdr= {'User-Agent': 'Mozilla/5.0'}
site= "https://lectortmo.com"

def find_url(text):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,text)       
    return( [x[0] for x in url])

def get_populars():
    doc=pq(site, parser = 'html',  headers=hdr)
    populars=doc.find("#pills-populars > div:nth-child(1) > div")
    results=[]
    for manga in populars.items():
        info={}
        info['link']= manga.find(" a ").attr("href"),
        info['poster']=find_url(manga.find("a > div > style").text())
        info['title']=manga.find("a > div > div > h4").attr('title')
        info['genre']=manga.find("a > div >span:nth-child(5)").text()
        results.append(info)

    
    return results


queries={'_page':1,'title':"boku no hero" }

def search(title, page=1):
    queries={'_page':page,'title':title}
    url=requests.get(site+'/library', params=queries, headers=hdr)
    doc= pq(url.url, headers=hdr)
    results=doc.find("#app > main > div:nth-child(2) > div.col-12.col-lg-8.col-xl-9 > div:nth-child(3) > div")
    resultList=[]
    for result in results.items():
        article={
        'link':result.find("a").attr('href'),
        'img': find_url(result.find('a > div > style').text()),
        'title':result.find(' a > div > div > h4').attr('title'),
        'genre':result.find('a > div > span:nth-child(5)').attr('title')
        }
        resultList.append(article)
    return resultList

        
#app > main > div:nth-child(2) > div.col-12.col-lg-8.col-xl-9 > div:nth-child(3) > div:nth-child(3) > a > div > span:nth-child(3)
#app > main > div:nth-child(2) > div.col-12.col-lg-8.col-xl-9 > div:nth-child(3) > div:nth-child(1) > a > div > span.demography.josei

def get_episodeList(link):
    doc= pq(link, headers=hdr)
    chapters=doc.find("#chapters > ul > li") 
    extraChapers=doc.find("#chapters-collapsed > li")

    chapterList=[]
    for chapter in chapters.items():

        titulo= chapter.find("h4 > div > div.col-10.text-truncate > a ").text()
        link=chapter.find("div > div > ul > li > div > div.col-2.col-sm-1.text-right > a").attr("href")
        article={
            "title":titulo,
            "link":link
        }
        chapterList.append(article)

    for chapter in extraChapers.items():
        titulo= chapter.find("h4 > div > div.col-10.text-truncate > a ").text()
        link=chapter.find("div > div > ul > li > div > div.col-2.col-sm-1.text-right > a").attr("href")
        article={
            "title":titulo,
            "link":link
        }
        chapterList.append(article)

    return chapterList


def get_images(link):
    doc=pq(link, headers=hdr).find("#app > header > nav > div > div:nth-child(4) > a").attr("href")
    doc=pq(doc, headers=hdr)
    images=doc.find("#main-container > div")
    imageList=[]
    for image in images.items():
        imageList.append(image.find("img").attr("data-src"))
    return imageList
