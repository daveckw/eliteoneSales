#for manipulating db in python console
from run import create_app
from app import db
from app.models import User, Post, UserSale, ProjectSale, Project
from sqlalchemy.sql import func

app = create_app()
ctx = app.app_context()
ctx.push()


