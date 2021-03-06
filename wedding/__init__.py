from flask import Flask
from flask.ext.mail import Mail

app = Flask(__name__.split('.')[0])
app.config.from_object('wedding.envconf')
mail = Mail(app)

if not app.debug:
    import logging
    from logging.handlers import SMTPHandler

    mail_handler = SMTPHandler((app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
        app.config['MAIL_DEFAULT_SENDER'],
        'alex@alexluke.me',
        'Exception on wedding site',
        credentials=(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD']))
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)

import views
