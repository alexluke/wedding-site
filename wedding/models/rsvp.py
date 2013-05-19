from wedding.models import db, BaseFields

class RSVP(BaseFields, db.Model):
    name = db.Column(db.String(255))
    email = db.Column(db.String(512))
    attending = db.Column(db.Boolean)
    message = db.Column(db.Text)
    num_adult_guests = db.Column(db.Integer)
    num_child_guests = db.Column(db.Integer)
    attending_ceremony = db.Column(db.Boolean)
    attending_reception = db.Column(db.Boolean)
    vegetarian = db.Column(db.Boolean)
    gluten_free = db.Column(db.Boolean)
    other_dietary = db.Column(db.Text)

class PotluckDish(BaseFields, db.Model):
    rsvp_id = db.Column(db.Integer, db.ForeignKey(RSVP.id), nullable=False)
    course = db.Column(db.String(50))
    dish = db.Column(db.String(255))

    rsvp = db.relationship(RSVP, backref=db.backref('dishes'))
