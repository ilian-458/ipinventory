# Script pour créer un utilisateur admin de test
from app import app, db
from app.models import User
from werkzeug.security import generate_password_hash

with app.app_context():
    # Vérifier si l'admin existe déjà
    admin = User.query.filter_by(email='admin@test.com').first()
    
    if admin:
        print("L'utilisateur admin existe déjà!")
    else:
        # Créer l'utilisateur admin
        admin = User(
            email='admin@test.com',
            password=generate_password_hash('admin123'),
            role='admin'
        )
        db.session.add(admin)
        db.session.commit()
        print("Utilisateur admin créé avec succès!")
        print("Email: admin@test.com")
        print("Mot de passe: admin123")
