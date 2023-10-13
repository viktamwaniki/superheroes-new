from datetime import datetime
from sqlalchemy import DateTime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from config import db


class heroPower(db.Model):
    # _tablename_ = 'heroPowers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('power.id'))
    created_at = db.Column(DateTime, default=datetime.utcnow)
    updated_at = db.Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

   
    
    def _init_(self, strength, power, hero):  
        self.strength = strength
        self.hero_id = hero.id
        self.power_id = power.id
       

    def _repr_(self):
        return f'<Hero(name={self.name}, super_name={self.super_name})>'

    @validates('strength')
    def validate_strength(self, key, value):
        strengths = ['Weak', 'Strong', 'Average']
        if not value:
            return ValueError('should not be empty')
        if len(value) > 50:
            return ValueError('Strength was more than 50 characters length')
        if value not in strengths:
            raise ValueError("Strength should either be ['Weak', 'Strong', 'Average']")
        return value

