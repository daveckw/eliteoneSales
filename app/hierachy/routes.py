# app/hierachy/routes.py

from flask import render_template, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from app.models import Post, User

hierachy = Blueprint('hierachy', __name__)

@hierachy.route("/hierachy")
@login_required
def check_hierachy():
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=current_user.username).first()
    downlines = user.downline
    return render_template('hierachy.html', downlines=downlines, user=user)

