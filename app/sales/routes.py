# app/sales/routes.py

from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import login_user, current_user, logout_user, login_required
from app.models import User, Post, UserSale, ProjectSale, Project
from app.sales.forms import SaleForm, ProjectForm
from app import db

sales = Blueprint('sales', __name__)


@sales.route("/create_sale", methods=['GET', 'POST'])
@login_required
def create_sale():
    form = SaleForm()
    form.ren1.choices = [(ren1.id, ren1.username) for ren1 in User.query.all()]
    form.project.choices = [(project.id, project.name) for project in Project.query.all()]
    if form.validate_on_submit():
        user = User.query.filter_by(username=current_user.username).first()
        project_id = form.project.data
        psale = ProjectSale(date_posted=form.date_posted.data,
                            unit_number=form.unit_number.data,
                            size=form.size.data,
                            buyer=form.buyer.data,
                            spaprice=form.spaprice.data,
                            netprice=form.netprice.data,
                            project_id=project_id,
                            package=form.package.data,
                            remark=form.remark.data,
                            created_by=current_user.username)

        db.session.add(psale)
        db.session.commit()  

        project_sale_id = psale.id
        user_id = form.ren1.data
        netvalue = float(form.ren1perc.data) / 100 * float(form.netprice.data)
        commission = netvalue * 0.02
        usersale = UserSale(user_id=user_id,
                            percentage=form.ren1perc.data,
                            netvalue=netvalue,
                            project_sale_id=project_sale_id,
                            commission=commission)
                            

        db.session.add(usersale)
        db.session.commit()     

        flash('Your sale has been created!', 'success')
        return redirect(url_for('main.home'))
    
    return render_template('create_sale.html', title='New Sale',
                           form=form, legend='New Sale')

@sales.route("/project", methods=['GET', 'POST'])
@login_required
def new_project():
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(name=form.name.data, location=form.location.data)
        db.session.add(project)
        db.session.commit()
        flash('Your project has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('test.html', title='New Project',
                            form=form, legend='New Project')


#Display User Sales Table
@sales.route("/display_sales", methods=['GET'])
@login_required
def display_sales():
    user = current_user
    usersale = UserSale.query.filter_by(user_id=user.id).all()
    return render_template('display_sales.html', usersale=usersale, user=user)
