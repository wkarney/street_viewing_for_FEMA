from flask import render_template, flash, redirect, request, send_from_directory
from app import app
from app.forms import LoginForm
from app.forms import ContactForm
from flask_uploads import UploadSet, configure_uploads, IMAGES

# API keys
import app.keys as keys

# Package imports for dealing with images
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

# Package imports for Zillow
from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults

# Package imports for Google Maps APIs
import google_streetview.api

# Geocoding and reverse Geocoding
from pygeocoder import Geocoder

# User defined functions
from app.functions import get_gps_details, convert_to_degress, get_img_coord_str, get_img_coord_tuple, pull_streetview, reverse_lookup, zillow_query


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

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
@app.route('/upload', methods=['GET', 'POST'])
def upload():

    if request.method == 'POST' and 'photo' in request.files:
        # Save uploaded file
        filename = photos.save(request.files['photo'])

        # Use current photo to pull streetview photo
        current_photo = Image.open(request.files['photo'])
        pull_streetview(get_img_coord_str(current_photo), key=keys.google)
        sview_photo = 'gsv_0.jpg'

        # Render and return form page with photos
        form = ContactForm()
        return render_template('contact.html', form=form, image_name=filename, image_name2=sview_photo)
    return render_template('upload.html')


@app.route('/app/<filename>')
def send_image(filename):
    return send_from_directory("img", filename)
