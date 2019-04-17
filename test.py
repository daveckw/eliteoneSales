#Testing script for manipulating db in python console
from run import create_app
from app import db
from app.models import User, Post, UserSale, ProjectSale, Project
from sqlalchemy.sql import func

app = create_app()
ctx = app.app_context()
ctx.push()

def SumValue(self):
    sum = 0
    for x in self:
        print('Project: {} | Unit No: {} | Net Price: RM{} | Commission: RM{}'\
            .format(x.project_sale.project.name, x.project_sale.unit_number, x.project_sale.netprice, x.commission))
        sum = sum + x.netvalue
    print("The total sum is RM{}".format(sum))
    print('---------')

##Aaron Sales
username = 'aaron'
userid = User.query.filter_by(username=username).scalar().id
print("User is {} | userid is {}".format(username, userid))
usersale = UserSale.query.filter_by(user_id=userid)
SumValue(usersale)

#Dave Sales
username = 'dave'
userid = User.query.filter_by(username=username).scalar().id
print("User is {} | userid is {}".format(username, userid))
usersale = UserSale.query.filter_by(user_id=userid)
SumValue(usersale)

#Create Dropdown List
def CreateDropDown(self):
    list1 = [(x.id, x.username) for x in self.query.all()]
    for x in list1:
        print(x[0], x[1])

CreateDropDown(User)









