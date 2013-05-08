import sys, os

sys.path.append(os.getcwd())

from wedding import app
from wedding.models import db

db.create_all()
app.run()
