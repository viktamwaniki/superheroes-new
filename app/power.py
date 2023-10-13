from datetime import datetime
from sqlalchemy import DateTime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from config import db

class Power(db.Model):
    # _tablename_ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256),nullable = False)
    description = db.Column(db.String)
    created_at = db.Column(DateTime, default = datetime.utcnow)
    updated_at = db.Column(DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)

    heros= db.relationship('heroPower', backref= db.backref('powers'))

    @validates('description')
    def validate_description(self, key, value):
        if not value:
            raise ValueError("Description should be present.")
        if len(value) < 20:
            raise ValueError("Description should atleast have a length of 20 characters.")
        return value

    def _init_(self, name, description): 
        self.name = name
        self.description = description

    def _repr_(self):
        return f'<Power(name={self.name}, description={self.description})>'

