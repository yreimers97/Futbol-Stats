#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, City

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        City.query.delete()
        print("Starting seed...")
        city1 = City(name='Phuket', country='Thailand', continent='Asia')
        city2 = City(name='Istanbul', country='Turkey', continent='Europe/Asia')

        db.session.add_all([city1, city2])
        db.session.commit()
        print("Added info")
