from flask import Flask
from flask.ext.mail import Mail

app = Flask(__name__.split('.')[0])
app.config.from_object('wedding.envconf')
mail = Mail(app)

import views
