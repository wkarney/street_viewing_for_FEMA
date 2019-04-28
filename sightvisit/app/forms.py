# request wtf and flask forms
from flask_wtf import FlaskForm, Form
# request assortmemt of field options for forms
from wtforms import TextField, IntegerField, TextAreaField, StringField, PasswordField, BooleanField, SubmitField, RadioField, SelectField
# request for valid info in TextField
from wtforms.validators import DataRequired
# request for display error
from wtforms import validators, ValidationError

# Login form with fields
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
# Contect for template used for Disaster Form
class ContactForm(Form):
   name = TextField("Owner Name:",[validators.Required("Please enter your name.")])
   Homes = SelectField('House Type (Conventional/Manufactured):', choices = [('C','Conventional'),('M','Manufactured')])
   Insurance = SelectField('Does the homeowner have insurance?', choices = [('Y','Yes'),('N','No'),('P','Partial')])
   Flood_Plain = SelectField('Is the property in a flood plain?', choices = [('Y','Yes'),('N','No')])
   Flood_Insurance = SelectField('Does the homeowner have flood insurance?', choices = [('Y','Yes'),('N','No')])
   Address = TextField("Address:")
   Zip_Code = TextField('Zipcode:')
   State = SelectField('State/Territory:', choices = [("Alabama","Alabama"),("Alaska","Alaska"),("Arizona","Arizona"),("Arkansas","Arkansas"),("California","California"),("Colorado","Colorado"),("Connecticut","Connecticut"),("Delaware","Delaware"),("Florida","Florida"),("Georgia","Georgia"),("Hawaii","Hawaii"),("Idaho","Idaho"),("Illinois","Illinois"),("Indiana","Indiana"),("Iowa","Iowa"),("Kansas","Kansas"),("Kentucky","Kentucky"),("Louisiana","Louisiana"),("Maine","Maine"),("Maryland","Maryland"),("Massachusetts","Massachusetts"),("Michigan","Michigan"),("Minnesota","Minnesota"),("Mississippi","Mississippi"),("Missouri","Missouri"),("Montana","Montana"),("Nebraska","Nebraska"),("Nevada","Nevada"),("New Hampshire","New Hampshire"),("New Jersey","New Jersey"),("New Mexico","New Mexico"),("New York","New York"),("North Carolina","North Carolina"),("North Dakota","North Dakota"),("Ohio","Ohio"),("Oklahoma","Oklahoma"),("Oregon","Oregon"),("Pennsylvania","Pennsylvania"),("Puerto Rico","Puerto Rico"),("Rhode Island","Rhode Island"),("South Carolina","South Carolina"),("South Dakota","South Dakota"),("Tennessee","Tennessee"),("Texas","Texas"),("Utah","Utah"),("Vermont","Vermont"),("Virginia","Virginia"),("Washington","Washington"),("West Virginia","West Virginia"),("Wisconsin","Wisconsin"),("Wyoming","Wyoming")])
   Flood_NonFlood = SelectField('Damage (Flood/Non-Flood)?', choices = [('fld', 'Flood'),('nfld', 'Non-Flood')])
   Damage_Level = SelectField('Damage Level', choices = [('Inex', 'Inaccessible'),
      ('ds', 'Destroyed'),('maj', 'Major'),('min', 'Minor'),('aff', 'Affected')])
   email = TextField("Email: ",[validators.Required("Please enter your email address."),
      validators.Email("Please enter your email address.")])
   submit = SubmitField("Send")

# Source: Miguel Grinberg https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
# Source: Lalith Polepeddi https://code.tutsplus.com/tutorials/intro-to-flask-adding-a-contact-page--net-28982
