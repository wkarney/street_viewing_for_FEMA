from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config['UPLOADED_PHOTOS_DEST'] = '/Users/orah82/streetview_2/app/static/img'



from app import routes
