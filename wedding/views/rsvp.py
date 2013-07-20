from flask import request, flash, redirect, url_for, session, render_template
from flask.ext.mail import Message
from wedding import app, mail
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

        if attending:
            if not any([field in ('attending_ceremony', 'attending_reception') for field in request.form]):
                errors['attending_any'] = 'You should really come to at least one of these'

            try:
                if int(request.form['num_adult_guests']) < 0:
                    errors['attending'] = 'Please enter a number'
            except ValueError:
                errors['attending'] = 'Please enter a number'
            try:
                if int(request.form['num_child_guests']) < 0:
                    errors['attending'] = 'Please enter a number'
            except ValueError:
                errors['attending'] = 'Please enter a number'

        if len(errors) == 0:
            rsvp = RSVP()
            rsvp.name = request.form['name']
            rsvp.email = request.form['email']
            rsvp.attending = attending
            if attending:
                rsvp.num_adult_guests = int(request.form['num_adult_guests'])
                rsvp.num_child_guests = int(request.form['num_child_guests'])
                rsvp.attending_ceremony = 'attending_ceremony' in request.form
                rsvp.attending_reception = 'attending_reception' in request.form
                rsvp.vegetarian = 'vegetarian' in request.form
                rsvp.gluten_Free = 'gluten_free' in request.form
                rsvp.other_dietary = request.form['other_dietary']
            else:
                rsvp.message = request.form['message']

            db.session.add(rsvp)
            db.session.commit()
            session['rsvp_id'] = rsvp.id

            msg = Message("RSVP submission", recipients=['alex@alexluke.me', 'colettesonafrank@hotmail.com'])
            if rsvp.attending:
                msg.body = render_template('email/rsvp_attending.txt', rsvp=rsvp)
            else:
                msg.body = render_template('email/rsvp_not_attending.txt', rsvp=rsvp)

            mail.send(msg)

            if rsvp.attending:
                return redirect(url_for('potluck'))
            else:
                return redirect(url_for('home'))

        return dict(form=request.form, errors=errors)

    return dict(form={})

@app.route('/potluck', methods=['GET', 'POST'])
@templated()
def potluck():
    if 'rsvp_id' not in session:
        rsvp = None
    else:
        rsvp = RSVP.query.get(session['rsvp_id'])

    if request.method == 'POST':
        errors = dict()
        if not rsvp:
            if not request.form['email']:
                errors['email'] = 'Email is required'
            else:
                rsvp = RSVP.query.filter_by(email=request.form['email']).first()
                if not rsvp:
                    errors['email'] = "This email address hasn't RSVP'd yet."

        if 'course' not in request.form:
            errors['course'] = 'What type of dish are you bringing?'

        if not request.form['dish']:
            errors['dish'] = 'What are you bringing?'

        if 'servings' not in request.form:
            errors['servings'] = 'Please enter the number of servings in your dish'
        elif request.form['servings']:
            try:
                if int(request.form['servings']) < 0:
                    errors['servings'] = 'Please enter a number'
            except ValueError:
                errors['servings'] = 'Please enter a number'

        if len(errors) == 0:
            dish = PotluckDish()
            dish.rsvp = rsvp
            dish.course = request.form['course']
            dish.dish = request.form['dish']
            dish.servings = request.form['servings']
            dish.vegetarian = 'vegetarian' in request.form
            dish.gluten_free = 'gluten_free' in request.form

            db.session.add(dish)
            db.session.commit()

            flash('Thanks for bring a dish for the potluck!', 'success')
            return redirect(url_for('potluck'))

        return dict(form=request.form, rsvp=rsvp, errors=errors)

    form = dict()

    dishes = PotluckDish.query.all()
    return dict(form=form, rsvp=rsvp, dishes=dishes)
