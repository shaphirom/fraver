from flask import Blueprint, render_template, url_for, redirect, request, session, flash

from model.users import User
from utils.db import db

from forms.userForm import userForm
from forms.loginForm import loginForm

users = Blueprint('users', __name__ )

@users.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        nameForm = request.form.get('name')
        emailForm = request.form.get('email')
        userLogin = User.query.filter_by( name = nameForm ).first()
        if userLogin != None:
            if userLogin.email == emailForm :
                session['user'] = userLogin.email
                flash('Login Correcto')
                return redirect(url_for('users.main'))
        flash('Datos Incorrectos')
        return redirect(url_for('users.login'))

    form = loginForm()
    return render_template('login.html',form=form)

@users.route('/logout')
def logout():
    session.pop('user',None)
    return redirect(url_for('users.main'))

@users.route('/')
def main():
    try:
        if session['user'] != None:
            
            form = userForm()
            lista = User.query.all()
            return render_template('users.html',form = form,users = lista)
        
    except:
        return redirect(url_for('users.login'))
        
    

@users.route('/add', methods = ['POST','GET'])
def add():
    try:
        if session['user'] != None:
            if request.method == 'POST':
                admin = User(name = request.form.get('name'), email = request.form.get('email') )
                db.session.add(admin)
                db.session.commit()
                return redirect(url_for('users.main'))
            
            print("Nada ocurrio")
            return redirect(url_for('users.main'))
    except:
        return redirect(url_for('users.login'))


@users.route('/user/update/<id>', methods=['GET','POST'])
def updateData(id):
    try:
        if session['user'] != None:
            user = User.query.get(id)
            form = userForm()
            
            if request.method == 'POST':
                user.name = request.form.get('name')
                user.email = request.form.get('email')
                db.session.commit()
                
                return redirect(url_for('users.main'))
            
            return render_template('usersEdit.html',form = form, user = user)
    except:
        return redirect(url_for('users.login'))

@users.route('/user/delete/<id>')
def deleteData(id):
    try:
        if session['user'] != None:
            user = User.query.get(id)
            db.session.delete(user)
            db.session.commit()
            return redirect(url_for('users.main'))
    except:
        return redirect(url_for('users.login'))
