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
   name = TextField("Name Of Resident",[validators.Required("Please enter your name.")])
   Homes = RadioField('Homes', choices = [('C','Conventional'),('M','Manufactured')])
   Insurance = RadioField('Insurance', choices = [('Y','Yes'),('N','No')])
   Flood_Plain = RadioField('Flood Plain', choices = [('Y','Yes'),('N','No')])
   Flood_Insurance = RadioField('Flood Insurance', choices = [('Y','Yes'),('N','No')])
   Address = TextAreaField("Address")
   Zip_Code = TextField('Zipcode')
   State = SelectField('State', choices = [("Alabama","Alabama"),("Alaska","Alaska"),("Arizona","Arizona"),("Arkansas","Arkansas"),("California","California"),("Colorado","Colorado"),("Connecticut","Connecticut"),("Delaware","Delaware"),("Florida","Florida"),("Georgia","Georgia"),("Hawaii","Hawaii"),("Idaho","Idaho"),("Illinois","Illinois"),("Indiana","Indiana"),("Iowa","Iowa"),("Kansas","Kansas"),("Kentucky","Kentucky"),("Louisiana","Louisiana"),("Maine","Maine"),("Maryland","Maryland"),("Massachusetts","Massachusetts"),("Michigan","Michigan"),("Minnesota","Minnesota"),("Mississippi","Mississippi"),("Missouri","Missouri"),("Montana","Montana"),("Nebraska","Nebraska"),("Nevada","Nevada"),("New Hampshire","New Hampshire"),("New Jersey","New Jersey"),("New Mexico","New Mexico"),("New York","New York"),("North Carolina","North Carolina"),("North Dakota","North Dakota"),("Ohio","Ohio"),("Oklahoma","Oklahoma"),("Oregon","Oregon"),("Pennsylvania","Pennsylvania"),("Rhode Island","Rhode Island"),("South Carolina","South Carolina"),("South Dakota","South Dakota"),("Tennessee","Tennessee"),("Texas","Texas"),("Utah","Utah"),("Vermont","Vermont"),("Virginia","Virginia"),("Washington","Washington"),("West Virginia","West Virginia"),("Wisconsin","Wisconsin"),("Wyoming","Wyoming")])
   Flood_NonFlood = SelectField('Flood or Non-Flood Damage', choices = [('fld', 'Flood Damage'),('nfld', 'Non-Flood Damage')])
   Damage_Level = SelectField('Damage Level', choices = [('Inex', 'Inaccessible'),
      ('ds', 'Destroyed'),('maj', 'Major'),('min', 'Minor'),('aff', 'Affected')])
   email = TextField("Email",[validators.Required("Please enter your email address."),
      validators.Email("Please enter your email address.")])
   submit = SubmitField("Send")
