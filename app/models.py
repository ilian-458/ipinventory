# Fichier: app/models.py
from app import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=False, default='user')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)
    
    # Relation avec les réservations
    reservations = db.relationship('Reservation', backref='user', lazy=True)
    
    def __repr__(self):
        return f'<User {self.email}>'


class Item(db.Model):
    __tablename__ = 'items'
    
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    reference = db.Column(db.String(100), unique=True, nullable=False)
    status = db.Column(db.String(50), nullable=False, default='available')
    
    # Relation avec les réservations
    reservations = db.relationship('Reservation', backref='item', lazy=True)
    
    def __repr__(self):
        return f'<Item {self.name}>'


class Reservation(db.Model):
    __tablename__ = 'reservation'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    reserved_at = db.Column(db.DateTime, default=datetime.utcnow)
    start_reservation = db.Column(db.DateTime, nullable=False)
    end_reservation = db.Column(db.DateTime, nullable=False)
    
    def __repr__(self):
        return f'<Reservation {self.id}>'
