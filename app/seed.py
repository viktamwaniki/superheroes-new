import sys
import os
# Adjust the path to the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import db
from hero import  Hero
from power import Power
from heroPower import heroPower
from app import app

import random

with app.app_context():

 print(" Seeding powers...")
 powers_data = [
    {"name": "super strength", "description": "gives the wielder super-human strengths"},
    {"name": "kick", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
    {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
    {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
 ]

 for power_info in powers_data:
     power = Power(**power_info)
     db.session.add(power)

  
 print("Seeding heroes...")
 heroes_data = [
    {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
    {"name": "Doreen Green", "super_name": "Squirrel Girl"},
    {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
    {"name": "Janet Van Dyne", "super_name": "The Wasp"},
    {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
    {"name": "Carol Danvers", "super_name": "Captain Marvel"},
    {"name": "Jean Grey", "super_name": "Dark Phoenix"},
    {"name": "Ororo Munroe", "super_name": "Storm"},
    {"name": "Kitty Pryde", "super_name": "Shadowcat"},
    {"name": "Elektra Natchios", "super_name": "Elektra"}
 ]

 for hero_info in heroes_data:
    hero = Hero(**hero_info)
    db.session.add(hero)


 print(" Adding powers to heroes...")
 strengths = ["Strong", "Weak", "Average"]
 heroes = Hero.query.all()

 for hero in heroes:
    for _ in range(random.randint(1, 4)):
        power = Power.query.order_by(db.func.random()).first()
        hero_power = heroPower(hero_id=hero.id, power_id=power.id, strength=random.choice(strengths))
        db.session.add(hero_power)


 try:
    db.session.commit()
    print("Seeding Successful!")
 except Exception as e:
    db.session.rollback()
    print("Error:", str(e))
