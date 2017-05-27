from flask import Flask, render_template, request, flash
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

class TextProcessorForm(Form):
    name = TextAreaField('Name: ', validators=[validators.required()])
