from flask_wtf import FlaskForm, Form
from wtforms import TextField, IntegerField, TextAreaField, StringField, PasswordField, BooleanField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired
from wtforms import validators, ValidationError

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class ContactForm(Form):
   name = TextField("Name Of Student",[validators.Required("Please enter your name.")])
   Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
   Address = TextAreaField("Address")

   email = TextField("Email",[validators.Required("Please enter your email address."),
      validators.Email("Please enter your email address.")])

   Age = IntegerField("age")
   language = SelectField('Languages', choices = [('cpp', 'C++'),
      ('py', 'Python')])
   submit = SubmitField("Send")
