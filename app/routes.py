# Fichier: app/routes.py
from flask import render_template
from app import app

@app.route('/')
def index():
    # Redirige vers la page de login par défaut
    return render_template('login.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')