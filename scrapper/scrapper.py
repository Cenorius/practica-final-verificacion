#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import requests
import StringIO
from lxml import etree

def get_articles_by_date(date):
    # result will have a list of dicts with articles title as key and URL as value
    articles = list()
    parser = etree.HTMLParser()

    # All dates URL will start with this pattern
    URL = "http://elpais.com/tag/fecha/"
    # the date comes with the following formar dd/mm/yyyy
    d = date.split("/")
    if len(d) != 3:
        raise Exception("invalid date format")
    URL += d[2] + d[1] + d[0]
        

    r = requests.get(URL)
    if r.status_code != 200:
        raise Exception("something went wrong, status code != 200 OK. Status code: %d" % r.status_code)

    resp = r.text
    try:
        tree = etree.parse(StringIO.StringIO(resp), parser=parser)
        titles = map(unicode, tree.xpath('//h2[@class="articulo-titulo"]/a/text()'))
        articles_urls = tree.xpath('//h2[@class="articulo-titulo"]/a/@href')

    except Exception, e:
        raise Exception("body doesn't contain valid HTML")

    for t, u in zip(titles, articles_urls):
        d = {"title": unicode(t), "url": "http:"+u}
        articles.append(d)
    return articles

def get_article_body(url):
    parser = etree.HTMLParser()
    content = ""
    r = requests.get(url)
    if r.status_code != 200:
        raise Exception("something went wrong, status code != 200 OK. Status code: %d" % r.status_code)
    resp = r.text

    tree = etree.parse(StringIO.StringIO(resp), parser=parser)
    body = tree.xpath('//*[@id="cuerpo_noticia"]/p')

    for element in body:
        content+= recursive_get_text(element)

    try:
        introduction = tree.xpath('//*[@id="articulo-introduccion"]/p')
        for element in introduction:
            content+= recursive_get_text(element)
    except:
        pass

    return content

def recursive_get_text(element):
    if not isinstance(element,etree._Element):
        raise TypeError
    
    result=""

    for i in element.getchildren():
        result+=recursive_get_text(i)

    if(element.text):
        result += element.text

    return result + " "


