# Script pour initialiser la base de données
from app import app, db

with app.app_context():
    db.create_all()
    print("Base de données créée avec succès!")
