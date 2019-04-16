#for manipulating db in python console
from run import create_app
from app import db
from app.models import User, Post

app = create_app()
ctx = app.app_context()
ctx.push()