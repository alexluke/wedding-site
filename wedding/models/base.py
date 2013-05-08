import re
from sqlalchemy.sql.expression import func
from sqlalchemy.ext.declarative import declared_attr
from flask.ext.sqlalchemy import SQLAlchemy
from wedding import app

db = SQLAlchemy(app)

class BaseFields(object):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime, default=func.now(), onupdate=func.now())

    @declared_attr
    def __tablename__(cls):
        def _join(match):
            word = match.group()
            if len(word) > 1:
                return ('_%s_%s' % (word[:1], word[-1])).lower()
            return '_' + word.lower()
        return re.sub(r'([A-Z+)(?=[a-z0-9])', _join, cls.__name__).lstrip('_')
