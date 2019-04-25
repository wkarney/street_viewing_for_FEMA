from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config['UPLOADED_PHOTOS_DEST'] = 'app/img'



from app import routes
