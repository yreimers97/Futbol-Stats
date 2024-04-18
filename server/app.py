#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import City
# Views go here!
class AllCities(Resource):
    def get(self):
        response_body = [city.to_dict(only=('id', 'name', 'country', 'continent')) for city in City.query.all()]
        return make_response(response_body, 200)
api.add_resource(AllCities, '/cities')

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

if __name__ == '__main__':
    app.run(port=7777, debug=True)