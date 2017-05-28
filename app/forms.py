from flask import Flask, render_template, request, flash
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, DateField, RadioField

class TextProcessorForm(Form):
    date = DateField('Date: ', validators=[validators.required()])
    source = RadioField('Source', choices=[('Local','Process only already downloaded news'),('Remote','Get remote news and process them')])
