# Fichier: app/__init__.py
from flask import Flask

app = Flask(__name__)

# IMPORTANT : On importe les routes à la fin pour éviter les erreurs
from app import routes