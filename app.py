from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "4534gdghjk5d#$RGR^HDG"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def home():
    pets = Pet.query.all()
    print(pets)
    return render_template("index.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def show_pet_form():
    form = AddPetForm()
    # Is this a post request ? AND is the CSRF token is valid ?
    if form.validate_on_submit():
        # raise
        name = form.name.data
        species = form.species.data
        photo = form.photo.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo, age=age, notes=notes)

        print(pet)
        
        db.session.add(pet)
        db.session.commit(pet)
        return redirect("/")
    else:
        # if it is a get request or if the token is missing
        return render_template("add_pet_form.html", form=form)
