import datetime

from traitlets import ValidateHandler, validate
import db
from click import DateTime


class Hero(db.Model):
    _tablename_ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256),nullable = False)
    super_name = db.Column(db.String)
    created_at = db.Column(DateTime, default = datetime.utcnow)
    updated_at = db.Column(DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)

    powers = db.relationship('Power', secondary='heroPowers', back_populates='heroes')

    def _init_(self, name, super_name):
        self.name = name  
        self.super_name = super_name  

    def _repr_(self):
        return f'<Hero(name={self.name}, super_name={self.super_name})>'

class heroPower(db.Model):
    _tablename_ = 'heroPowers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
    created_at = db.Column(DateTime, default=datetime.utcnow)
    updated_at = db.Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    
    def _init_(self, strength, power, hero):  
        self.strength = strength
        self.hero_id = hero.id
        self.power_id = power.id
       

    def _repr_(self):
        return f'<Hero(name={self.name}, super_name={self.super_name})>'

    @validate('strength')
    def validate_strength(self, key, value):
        strengths = ['Weak', 'Strong', 'Average']
        if not value:
            return ValueError('should not be empty')
        if len(value) > 50:
            return ValueError('Strength was more than 50 characters length')
        if value not in strengths:
            raise ValueError("Strength should either be ['Weak', 'Strong', 'Average']")
        return value


class Power(db.Model):
    _tablename_ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256),nullable = False)
    description = db.Column(db.String)
    created_at = db.Column(DateTime, default = datetime.utcnow)
    updated_at = db.Column(DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)

    heroes = db.relationship('Hero', secondary='heroPowers', back_populates='powers')

    @ValidateHandler('description')
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

