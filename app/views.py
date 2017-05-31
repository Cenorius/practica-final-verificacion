from flask import render_template, flash, redirect, request
from app import app
from .forms import TextProcessorForm
from textprocessor import core

@app.route("/index")
@app.route("/", methods=['GET', 'POST'])
def parse_text():
    temp=[]
    resp = dict()
    form = TextProcessorForm(request.form)

    if request.method == 'POST':
        date = form.date.raw_data[0]
        temp=date.split('/')
        date=temp[1]+"/"+temp[0]+"/"+temp[2]

        if form.validate():
            print request.form['source']
            if request.form['source']=='MostUsed':
                print "palabras mas usadas"
            elif request.form['source']=='Articles':
                print "palabras por articulo"
    return render_template('index.html', form=form, response=resp, message=None)