from flask import Flask,request, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from heroPower import heroPower
from hero import Hero
from power import Power
from config import db



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return ''

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = []
    for hero in Hero.query.all():
        heroes_data = {
            "id" : hero.id,
            "name": hero.name,
            "super_name": hero.super_name,
        }
        heroes.append(heroes_data)
    return jsonify(heroes)

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero_by_id(id):
    hero = Hero.query.get(id)
    if hero is None:
        return jsonify({"error": "Hero does not exist"}), 404
    hero_data = {
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name,
        "powers": []
    }
    for power in hero.powers:
        pwr = db.session.get(Power,power.power_id)
        hero_powers_list = {
                "id": pwr.id,
                "name": pwr.name,
                "description": pwr.description
            }
        hero_data ["powers"].append(hero_powers_list)
    return jsonify(hero_data)

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    powers_list = [
        {
            "id": power.id,
            "name": power.name,
            "description": power.description
        }
        for power in powers
    ]
    return jsonify(powers_list)

@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if power is None:
        return jsonify({"error": "Power cannot be found"}), 404
    power_info = {
        "id": power.id,
        "name": power.name,
        "description": power.description
    }
    return jsonify(power_info)

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id): 
    power = Power.query.get(id)
    if power is None:
        return jsonify({"error": "Power does not exist"}), 404
    new_description = request.json.get('description')
    if not new_description or len(new_description) < 20:
        return jsonify({"errors": ['validation errors']}), 400
    power.description = new_description
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": ["validation errors"]}), 400
    
    updated_power_info = {
        "id": power.id,
        "name": power.name,
        "description": power.description
    }
    return jsonify(updated_power_info)



if __name__ == '__main__':

   app.run(port=5554)
