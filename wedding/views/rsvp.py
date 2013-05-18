from flask import request, flash, redirect, url_for
from wedding import app
from helpers import templated
from wedding.models import *

@app.route('/rsvp', methods=['GET', 'POST'])
@templated()
def rsvp():
    if request.method == 'POST':
        attending = False
        errors = dict()
        if not request.form['name']:
            errors['name'] = 'Name is required'
        if not request.form['email']:
            errors['email'] = 'Email is required'
        if not 'attending' in request.form:
            errors['attending'] = 'Please let us know if you will be attending'
        else:
            attending = request.form['attending'] == 'yes'

        if attending and not any([field in ('attending_ceremony', 'attending_reception') for field in request.form]):
            errors['attending_any'] = 'You should really come to at least one of these'

        if len(errors) == 0:
            rsvp = RSVP()
            rsvp.name = request.form['name']
            rsvp.email = request.form['email']
            rsvp.attending = attending
            if attending:
                rsvp.num_adult_guests = request.form['num_adult_guests']
                rsvp.num_child_guests = request.form['num_child_guests']
                rsvp.attending_ceremony = 'attending_ceremony' in request.form
                rsvp.attending_reception = 'attending_reception' in request.form
                rsvp.vegetarian = 'vegetarian' in request.form
                rsvp.gluten_Free = 'gluten_free' in request.form
                rsvp.other_dietary = request.form['other_dietary']
            else:
                rsvp.message = request.form['message']

            db.session.add(rsvp)
            db.session.commit()
            flash('Thanks for your RSVP.', 'success')
            return redirect(url_for('home'))

        return dict(form=request.form, errors=errors)

    return dict(form={})
