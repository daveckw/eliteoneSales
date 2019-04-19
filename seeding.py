from run import create_app
from app import db, bcrypt
from app.models import User, Post, UserSale, ProjectSale, Project
from sqlalchemy.sql import func
from flask import Flask, request, jsonify
from tablib import Dataset
from datetime import datetime

app = create_app()
ctx = app.app_context()
ctx.push()

data = Dataset().load(open('agents1.csv').read())

def Convert2Date(string,n):
    date_created = string[n]
    date_created = date_created[0:10]
    date_created = datetime.strptime(date_created, '%Y-%m-%d')
    return date_created

def Convert2Date2(string,n):
    date_created = string[n]
    date_created = date_created[0:10]
    date_created = datetime.strptime(date_created, '%d/%m/%Y')
    return date_created

def RemoveSpaces(data):
    string=data.replace(' ','')
    return string

# for x in data[1:]:
#     fullname = x[1]
#     username = x[2]
#     title = x[3]
#     ic_number = RemoveSpaces(x[4])
#     email = x[5]
#     phone_number = x[6]
#     birthday = Convert2Date2(x,7)
#     location = x[10]
#     date_created = Convert2Date(x,11)
#     hashed_password = bcrypt.generate_password_hash(email).decode('utf-8')
#     print('{} | {} | {} | {} | {} | {} | {} | {} | {}'.\
#         format(fullname, username, title, ic_number, email, phone_number, birthday, location, date_created))
#     user = User(fullname=fullname, username=username, title=title,
#                 ic_number=ic_number, email=email, phone_number=phone_number,
#                 birthday=birthday, location=location, date_created=date_created,
#                 password=hashed_password)
#     db.session.add(user)
#     db.session.commit()







