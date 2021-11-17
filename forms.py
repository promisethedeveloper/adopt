from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Email, Optional





class AddPetForm(FlaskForm):
    """Form for adding pets."""
    name = StringField("Pet name:", validators=[InputRequired(message="Pet name is required")])
    species = StringField("Species:", validators=[InputRequired(message="Specie of pet is required")])
    photo = StringField("Photo URL:")
    age = IntegerField("How old is the pet?")
    notes =  TextAreaField("Add some notes:", render_kw={"rows": 5, "cols": 11})
    





