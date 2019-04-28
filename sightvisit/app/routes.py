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
# route to home page
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Carol Evans'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Updated Images'
        },
        {
            'author': {'username': 'Stevie'},
            'body': 'Updated Images'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
# route to Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        ## User login details
        # flash('Login requested for user {}, remember_me={}'.format(
        #     form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
# route to user's site
@app.route('/sites')
def sites():
    user = {'username': 'Carol'}
    location = {'location': 'Paris'}
    posts = [
        {
            'site': {'location': 'New York'},
            'body': 'TBA'
        },
        {
            'site': {'location': ''},
            'body': 'TBA'
        }
    ]
    return render_template('sites.html', location=location ,title='Sites', user=user, posts=posts)
#route to Disaster form
@app.route('/form', methods = ['GET', 'POST'])
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
        try:
            gps_string = get_img_coord_str(current_photo)
        except:
            # output img without streeview
            pull_streetview("38.556","-76.41", key=keys.google)
        pull_streetview(get_img_coord_str(current_photo), key=keys.google)
        sview_photo = 'gsv_0.jpg'

        # Pull latitude and longitude data as floats
        coords = get_img_coord_tuple(current_photo)
        latitude = coords[0]
        longitude = coords[1]
        address_details = reverse_lookup(lat=latitude, long=longitude, key=keys.google)
        subj_address = address_details[0]
        subj_zipcode = address_details[1]
        subj_city = address_details[2]
        subj_state = address_details[3]

        # Pull zillow Data
        zillowresult = zillow_query(address=subj_address, zipcode=subj_zipcode, key=keys.zillow)
        house_type = zillowresult.home_type
        house_size = zillowresult.home_size
        num_beds = zillowresult.bedrooms
        num_baths = zillowresult.bathrooms
        est_value = zillowresult.zestimate_amount
        est_date = zillowresult.zestimate_last_updated
        val_desc = "Zestimate"
        if est_value == None:
            est_value = zillowresult.tax_value
            est_date = zillowresult.tax_year
            val_desc = "Tax Assessment"

        # Render and return form page with photos
        form = ContactForm()
        return render_template('contact.html', form=form, image_name=filename, image_name2=sview_photo, address=subj_address, zipcode=subj_zipcode, city=subj_city, state=subj_state, bldg_type=house_type, bldg_size=house_size, beds=num_beds, baths=num_baths, value=est_value, val_date=est_date, val_desc=val_desc)
    return render_template('upload.html')

@app.route('/app/<filename>')
def send_image(filename):
    return send_from_directory("img", filename)


# Source: Miguel Grinberg https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
