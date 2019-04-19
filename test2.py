#Testing script for manipulating db in python console
from run import create_app
from app import db
from app.models import User, Post, UserSale, ProjectSale, Project
from sqlalchemy.sql import func
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, IntegerField, SelectField, DecimalField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

app = create_app()
ctx = app.app_context()
ctx.push()

class MyForm(FlaskForm):
    date_created = DateField('Date')

form = MyForm()











