from flask import render_template, flash, redirect, request
from app import app
from .forms import TextProcessorForm
import pymongo

from textprocessor import core
from DBUtils import DBUtils
from scrapper import scrapper

URL_MONGO='mongodb://localhost:27017/'
DATA_BASE_NAME='words'

@app.route("/index")
@app.route("/", methods=['GET', 'POST'])
def parse_text():
    temp=[]
    articles_r =[]
    words_r=[]

    form = TextProcessorForm(request.form)

    if request.method == 'POST':

        if form.validate():
            db=DBUtils(pymongo.MongoClient(URL_MONGO)[DATA_BASE_NAME].collection)

            date = form.date.raw_data[0]
            temp=date.split('/')
            date=temp[1]+"/"+temp[0]+"/"+temp[2]
            if request.form['source']=='MostUsed':
                articles=scrapper.get_articles_by_date(date)
                for article in articles:
                    if not db.exists_article_in_db(article.get('title'),date):
                        words=scrapper.get_article_body(article.get('url'))
                        words=core.process(words)
                        db.insert_words(date,article.get('title'),words)
                words_r=db.get_words_from_date(date)

            elif request.form['source']=='Articles':
                articles=scrapper.get_articles_by_date(date)
                for article in articles:
                    if not db.exists_article_in_db(article.get('title'),date):
                        words=scrapper.get_article_body(article.get('url'))
                        words=core.process(words)
                        db.insert_words(date,article.get('title'),words)
                    articles_r.append({u"title":article.get("title"), u'words':db.get_words_from_article(date,article.get('title'))})
                    
                print articles_r[0]
    return render_template('index.html', form=form, words=words_r, articles=articles_r)