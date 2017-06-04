from flask import render_template, flash, redirect, request
from app import app
from .forms import TextProcessorForm
import pymongo
import datetime

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
    message=None

    form = TextProcessorForm(request.form)

    if request.method == 'POST':

        if form.validate():

            date = form.date.raw_data[0]
            temp=date.split('/')
            print temp, date
            date=temp[1]+"/"+temp[0]+"/"+temp[2]
            try:
                if (int(temp[2]) > datetime.datetime.today().year):
                    print "lanza anyo"
                    raise Exception("No future dates allowed")
                else:
                    if (int(temp[0]) > datetime.datetime.today().month and int(temp[2]) >= datetime.datetime.today().year):
                        print "lanza mes"
                        raise Exception("No future dates allowed")
                    else:
                        if (int(temp[1]) > datetime.datetime.today().day and int(temp[2]) >= datetime.datetime.today().year and int(temp[0]) >= datetime.datetime.today().month):
                            print "lanza dia"
                            raise Exception("No future dates allowed")

                db=DBUtils(pymongo.MongoClient(URL_MONGO)[DATA_BASE_NAME].collection)
                articles=scrapper.get_articles_by_date(date)

                for article in articles:
                    if not db.exists_article_in_db(article.get('title'),date):
                        words=scrapper.get_article_body(article.get('url'))
                        words=core.process(words)
                        db.insert_words(date,article.get('title'),words)

                if request.form['source']=='MostUsed':
                    words_r=db.get_words_from_date(date)

                elif request.form['source']=='Articles':
                    for article in articles:
                        articles_r.append({u"title":article.get("title"), u'words':db.get_words_from_article(date,article.get('title'))})

            except Exception,e:
                message=str(e)
                return render_template('index.html', form=form, words=words_r, articles=articles_r, message=message)
<<<<<<< Updated upstream
        
        else:
            return render_template('index.html', form=form, message="You need to input a date and select an option")
    
=======

>>>>>>> Stashed changes
    return render_template('index.html', form=form, words=words_r, articles=articles_r, message=message)
