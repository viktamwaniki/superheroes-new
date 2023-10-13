from datetime import datetime
from sqlalchemy import DateTime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from config import db

class Hero(db.Model):
    # _tablename_ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256),nullable = False)
    super_name = db.Column(db.String)
    created_at = db.Column(DateTime, default = datetime.utcnow)
    updated_at = db.Column(DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)

    powers = db.relationship ('heroPower', backref=db.backref('heros'))

    def _init_(self, name, super_name):
        self.name = name  
        self.super_name = super_name  

    def hero_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'super_name': self.super_name,
            'powers': [hero_power.hero_dict() for hero_power in self.hero_powers]
        }
