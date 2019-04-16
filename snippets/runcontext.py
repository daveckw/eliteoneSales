#for manipulating db in python console
from run import create_app
from app import db
from app.models import User, Post, UserSale, ProjectSale, Project

app = create_app()
ctx = app.app_context()
ctx.push()

#run init script
project = Project(name='Millerz', location='KL')
db.session.add(project)
db.session.commit()

psale = ProjectSale(spaprice=1000000, netprice=900000, project_id=1)
db.session.add(psale)
db.session.commit()

usersale = UserSale(user_id=1, percentage=0.5, netvalue=450000, project_sale_id=1)
db.session.add(usersale)
db.session.commit()