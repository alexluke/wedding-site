import os

DEBUG = os.environ.get('DEBUG', False)
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SECRET_KEY = os.environ['SECRET_KEY']

MAIL_DEFAULT_SENDER = 'wedding@alexandcolette.com'
if 'MANDRILL_USERNAME' in os.environ:
    MAIL_SERVER = 'smtp.mandrillapp.com'
    MAIL_USERNAME = os.environ['MANDRILL_USERNAME']
    MAIL_PASSWORD = os.environ['MANDRILL_APIKEY']
else:
    MAIL_SERVER = os.environ['MAIL_SERVER']
    MAIL_USERNAME = os.environ['MAIL_USERNAME']
    MAIL_PASSWORD = os.environ['MAIL_PASSWORD']
MAIL_PORT = 465
MAIL_USE_SSL = True
