from flask.ext.uploads import Uploadset, configure_uploads, IMAGES


photos = Uploadset('photos', IMAGES)
configure_uploads(app, photos)
