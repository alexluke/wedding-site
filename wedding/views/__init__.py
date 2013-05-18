import os
from flask import abort, send_file
from wedding import app
from helpers import templated

import rsvp

@app.route('/')
@templated()
def home():
    pass

@app.route('/wedding-party')
@templated()
def wedding_party():
    pass

@app.route('/event-details')
@templated()
def details():
    pass

@app.route('/planning')
@templated()
def planning():
    pass

@app.route('/visiting-pdx')
@templated()
def visiting():
    pass

@app.route('/registry')
def registry():
    pass

@app.route('/contact-us')
def contact():
    pass

@app.context_processor
def get_nav():
    return dict(navigation=[
        ('home', 'Home'),
        ('wedding_party', 'Wedding Party'),
        ('details', 'Event Details'),
        ('planning', 'Planning'),
        ('visiting', 'Visiting Portland'),
        ('registry', 'Registry'),
        ('contact', 'Contact Us'),
    ])

# Serve the components when in debug mode.
# They will be concatted and minified in
# live mode.
if app.debug:
    @app.route('/components/<path:filename>')
    def components(filename):
        filename = os.path.join(os.getcwd(), 'components', filename)
        if not os.path.isfile(filename):
            abort(404)
        return send_file(filename)

