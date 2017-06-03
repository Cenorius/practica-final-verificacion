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
    try:
        d = date.split("/")
        URL += d[2] + d[1] + d[0]
    except Exception, e:
        raise Exception("invalid date format")

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
    body = tree.xpath('//*[@id="cuerpo_noticia"]/p/text()')
    try:
        introduction = tree.xpath('//*[@id="articulo-introduccion"]/p/text()')
        body += introduction
    except:
        pass

    try:
        extra_introduction = tree.xpath('//*[@id="articulo-introduccion"]/p/*')
        for i in extra_introduction:
            body.append(i.text)
    except:
        pass

    try:
        extra_body = tree.xpath('//*[@id="cuerpo_noticia"]/p/*')
        for i in extra_body:
            body.append(i.text)
    except:
        pass

    for i in body:
        content += i + " "
    return content

