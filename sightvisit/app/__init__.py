from flask import Flask
from config import Config
# Flask uses the location of the module passed here as
# a starting point when it needs to load associated resources such as
# template files
app = Flask(__name__)
app.config.from_object(Config)
app.config['UPLOADED_PHOTOS_DEST'] = 'app/img'



from app import routes
