from flask import Flask

app = Flask(__name__.split('.')[0])
app.config.from_object('envconf')

import views
