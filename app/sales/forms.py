# app/sales/forms.py

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, IntegerField, SelectField, DecimalField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from app.models import User


class SaleForm(FlaskForm):
    date_posted = DateField('Date', validators=[DataRequired()], format = '%d/%m/%Y')
    ren1 = SelectField('REN1',coerce=int, choices=[],validators=[DataRequired()])
    # ren2 = StringField('REN2', validators=[DataRequired()])
    ren1perc = IntegerField('REN1 %', validators=[DataRequired()])
    # ren2perc = IntegerField('REN2 %', validators=[DataRequired()])
    project = SelectField('Project Name',coerce=int, choices=[], validators=[DataRequired()])
    unit_number = StringField('Unit Name', validators=[DataRequired()])
    size = StringField('Size', validators=[DataRequired()])
    buyer = StringField('Buyer Name', validators=[DataRequired()])
    spaprice = DecimalField('SPA Price', validators=[DataRequired(message='Need to be a number')])
    netprice = DecimalField('Net Price', validators=[DataRequired(message='Need to be a number')])
    package = StringField('Package', validators=[DataRequired()])
    remark = StringField('Remark', validators=[DataRequired()])
    submit = SubmitField('Post')

class ProjectForm(FlaskForm):
    name = StringField('Name of Project', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    submit = SubmitField('Post')


# Sample
# Date: 2019-04-15
# REN 1: Eddie Wong (100.0%)
# Project: Ceylonz
# Unit No: 22-05
# Size: 578 sqft
# Buyer: Loo
# SPA Price: RM 1,009,140.00
# Nett Price: RM 842,631.90
# Booking Form: 
# Package: 16.5
# Remark: 
# Team: Eliteone

# WTforms package contains definitions of various form fields. Some Standard form fields are listed below.
# Sr.No	Standard Form Fields & Description
# 1	TextField
# Represents <input type = 'text'> HTML form element
# 2	BooleanField
# Represents <input type = 'checkbox'> HTML form element
# 3	DecimalField
# Textfield for displaying number with decimals
# 4	IntegerField
# TextField for displaying integer
# 5	RadioField
# Represents <input type = 'radio'> HTML form element
# 6	SelectField
# Represents select form element
# 7	TextAreaField
# Represents <testarea> html form element
# 8	PasswordField
# Represents <input type = 'password'> HTML form element
# 9	SubmitField
# Represents <input type = 'submit'> form element