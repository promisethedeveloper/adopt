from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"

# MODELS GO BELOW!
class Pet(db.Model):

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)


    name = db.Column(db.Text,
                   nullable=False)


    species = db.Column(db.Text, nullable=False)


    photo_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)


    age = db.Column(db.Integer, nullable=True)

    notes = db.Column(db.Text, nullable=True)

    available = db.Column(db.Text, nullable=True)


   

