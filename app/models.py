from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(20))
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    phone_number = db.Column(db.String(20), unique=True, nullable=False)
    ic_number = db.Column(db.String(20), unique=True)
    birthday = db.Column(db.DateTime)
    posts = db.relationship('Post', backref='author', lazy=True)
    upline_id = db.Column(db.Integer, db.ForeignKey('user.id'), index=True)
    upline = db.relationship(lambda: User, remote_side=id, backref='downline', foreign_keys = 'User.upline_id')
    referrer_id = db.Column(db.Integer, db.ForeignKey('user.id'), index=True)
    referrer = db.relationship(lambda: User, remote_side=id, backref='referree', foreign_keys = 'User.referrer_id')
    title = db.Column(db.String(20), nullable=False, default='REN')
    user_sale = db.relationship(lambda: UserSale, remote_side=id, backref='user')
    team = db.Column(db.String(50))
    location = db.Column(db.String(50))
    date_created = db.Column(db.DateTime,default=datetime.utcnow)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    location = db.Column(db.String(50), nullable=False)
    project_sale = db.relationship(lambda: ProjectSale, remote_side=id, backref='project')
    
    def __repr__(self):
        return f"Project('{self.name}')"

class ProjectSale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    unit_number = db.Column(db.String(50), nullable=False)
    size = db.Column(db.String(50), nullable=False)
    buyer = db.Column(db.String(100), nullable=False)
    spaprice = spaprice = db.Column(db.Float(), nullable=False)
    netprice = db.Column(db.Float(), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    user_sale = db.relationship(lambda: UserSale, remote_side=id, backref='project_sale')
    package = db.Column(db.String(100))
    remark = db.Column(db.Text)
    created_by = db.Column(db.Text)
    
    def __repr__(self):
        return f"ProjectSale('{self.project.name} RM{self.spaprice}')"

class UserSale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    percentage = db.Column(db.Float(), nullable=False)
    netvalue = db.Column(db.Float(), nullable=False)
    project_sale_id = db.Column(db.Integer, db.ForeignKey('project_sale.id'), nullable=False)
    commission = db.Column(db.Float)
    
    def __repr__(self):
        return f"UserSale('{self.id}')"