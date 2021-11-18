"""Seed file to make simple data for pets db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add pets
whiskey = Pet(name="Whiskey", species="dog", photo_url="https://images.unsplash.com/photo-1543466835-00a7907e9de1?ixid=MnwxMjA3fDB8MHxzZWFyY2h8Nnx8aGFwcHklMjBkb2d8ZW58MHx8MHx8&ixlib=rb-1.2.1&w=1000&q=80", age=4)
blue = Pet(name="Blue", species="cat", photo_url="https://media.istockphoto.com/photos/kitten-at-home-garden-wall-picture-id1273661469?b=1&k=20&m=1273661469&s=170667a&w=0&h=K-b-88J89oSBIwbD0WhhDoOvybcbjfePJoOHS0grHHA=", age=2)
fluffy = Pet(name="Fluffy", species="porcupine", photo_url="https://images.unsplash.com/photo-1605369179590-014a88d4560a?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8cG9yY3VwaW5lfGVufDB8fDB8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60", age=2)




# spike = Pet(name='Spike', species="porcupine")

# Add new objects to session, so they'll persist
db.session.add(whiskey)
db.session.add(blue)
db.session.add(fluffy)
# db.session.add(bowser)
# db.session.add(spike)

# Commit - otherwise, this never gets saved
db.session.commit()
