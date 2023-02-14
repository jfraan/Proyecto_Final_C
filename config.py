import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave_secreta'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:admin543@localhost/veterinaria'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
