from flask import render_template, flash, redirect, request
from app import app
from app.forms import LoginForm
from app.forms import ContactForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Omar'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Updated Images'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Updated Images'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/sites')
def sites():
    user = {'username': 'Omar'}
    location = {'location': 'Paris'}
    posts = [
        {
            'site': {'location': 'Michigan'},
            'body': 'TBA'
        },
        {
            'site': {'location': 'Texas'},
            'body': 'TBA'
        }
    ]
    return render_template('sites.html', location=location ,title='Sites', user=user, posts=posts)

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
   form = ContactForm()

   if request.method == 'POST':
    return 'Form posted.'

   elif request.method == 'GET':
        return render_template('contact.html', form=form)
