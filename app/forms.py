from flask import Flask, render_template, request, flash
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, DateField, RadioField

class TextProcessorForm(Form):
    date = DateField('Date: ',format='%m/%d/%Y', validators=[validators.required()])
    source = RadioField('Source', choices=[('MostUsed','Most used words'),('Articles','Words per article')])
