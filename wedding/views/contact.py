from flask import request, flash, redirect, url_for, session
from wedding import app
from helpers import templated
from wedding.models import *

@app.route('/contact-us', methods=['GET', 'POST'])
@templated()
def contact():
    if request.method == 'POST':
        form = request.form
        errors = dict()

        if not form['name']:
            errors['name'] = 'Name is required'
        if not form['email']:
            errors['email'] = 'Email is required'
        if not form['message']:
            errors['message'] = 'Message is required'

        if len(errors) == 0:
            # Send an email!
            flash('Thanks, we\'ll try to get back to you as soon as we can.', 'success')
            return redirect(url_for('home'))
        else:
            return dict(form=form, errors=errors)
    else:
        prepop = dict()
        if 'rsvp_id' in session:
            rsvp = RSVP.query.get(session['rsvp_id'])
            prepop['name'] = rsvp.name
            prepop['email'] = rsvp.email

        return dict(form=prepop)

