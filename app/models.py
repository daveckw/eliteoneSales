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
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    upline_id = db.Column(db.Integer, db.ForeignKey('user.id'), index=True)
    upline = db.relationship(lambda: User, remote_side=id, backref='downline')
    title = db.Column(db.String(20), nullable=False, default='REN')
    user_sale = db.relationship(lambda: UserSale, remote_side=id, backref='user')

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
    spaprice = spaprice = db.Column(db.Float(), nullable=False)
    netprice = db.Column(db.Float(), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    user_sale = db.relationship(lambda: UserSale, remote_side=id, backref='project_sale')
    
    def __repr__(self):
        return f"ProjectSale('{self.id}')"


class UserSale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    percentage = db.Column(db.Float(), nullable=False)
    netvalue = db.Column(db.Float(), nullable=False)
    project_sale_id = db.Column(db.Integer, db.ForeignKey('project_sale.id'), nullable=False)
    
    def __repr__(self):
        return f"UserSale('{self.id}')"