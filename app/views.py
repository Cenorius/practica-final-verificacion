from flask import render_template, flash, redirect, request
from app import app
from .forms import TextProcessorForm
from textprocessor import core

@app.route("/index")
@app.route("/", methods=['GET', 'POST'])
def parse_text():
    resp = dict()
    form = TextProcessorForm(request.form)
    if request.method == 'POST':
        text = request.form['name']
        if (len(text) > 100):
            #flash("Max length is 100")
            return render_template('index.html', form=form, response=None, message="Max length is 100")
        else:
            if form.validate():
                parsed_text = reversed(core.process(text))
                for i in parsed_text:
                    resp[i[0]] = i[1]
    return render_template('index.html', form=form, response=resp, message=None)