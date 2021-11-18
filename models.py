from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

DEFAULT_IMAGE_URL = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"

# MODELS GO BELOW!
class Pet(db.Model):
    """Adoptable pet."""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    name = db.Column(db.Text,
                   nullable=False)

    species = db.Column(db.Text, nullable=False)

    photo_url = db.Column(db.Text, default=DEFAULT_IMAGE_URL)

    age = db.Column(db.Integer, nullable=True)

    notes = db.Column(db.Text, nullable=True)

    available = db.Column(db.Boolean, nullable=False, default=True)


    def image_url(self):
        """Return image for pet -- bespoke or generic."""

        return self.photo_url or DEFAULT_IMAGE_URL



   

