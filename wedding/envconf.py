import os

DEBUG = os.environ.get('DEBUG', False)
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
