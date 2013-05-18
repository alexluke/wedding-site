from flask import request
from wedding import app
from helpers import templated
from wedding.models import *

@app.route('/rsvp', methods=['GET', 'POST'])
@templated()
def rsvp():
    if request.method == 'POST':
        pass
    return dict(form={})
