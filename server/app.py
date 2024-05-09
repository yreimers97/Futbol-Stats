#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, make_response
from flask_restful import Resource

# Local imports
from config import app, db, api

# Add your model imports

from models import User, Team, Player
# # Views go here!
class AllTeams(Resource):
    def get(self):
        response_body = [team.to_dict(only=('id', 'team_name', 'wins', 'draws', 'losses')) for team in Team.query.all()]
        return make_response(response_body, 200)
    
    def post(self):
        try:
            new_team = Team(name=request.json.get('team_name'))
            db.session.add(new_team)
            db.session.commit()
            response_body = new_team.to_dict(only=('id', 'team_name'))
            return make_response(response_body, 201)
        except:
            response_body = {
                "error": "Team must have a name."
            }
            return make_response(response_body, 400)

api.add_resource(AllTeams, '/teams')

class AllUsers(Resource):
    def get(self):
        response_body = [user.to_dict(only=('id', 'name', 'nationality', 'age')) for user in User.query.all()]
        return make_response(response_body, 200)
    
    def post(self):
        try:
            new_user = User(name=request.json.get('name', 'nationality', 'age'))
            db.session.add(new_user)
            db.session.commit()
            response_body = new_user.to_dict(only=('id', 'nationality', 'age'))
            return make_response(response_body, 201)
        except:
            response_body = {
                "error": "Not a valid input."
            }
            return make_response(response_body, 400)

api.add_resource(AllUsers, '/users')

class TeamByID(Resource):
    def get(self, id):
        team = db.session.get(Team, id)
        response_body = team.to_dict()
        return make_response(response_body, 200)
    
    def patch(self, id):
        team = Team.query.filter(Team.id == id).first()

        if(team):
            try:
                for attr in request.json:
                    setattr(team, attr, request.json[attr])
                
                db.session.commit()
                response_body = team.to_dict(only=('id', 'team_name', 'wins', 'draws', 'losses'))
                return make_response(response_body, 202)
            except:
                response_body = {
                    "errors": ["validation errors"]
                }
                return make_response(response_body, 400)
        else:
            response_body = {
                "error": "Team not found"
            }
            return make_response(response_body, 404)

    def delete(self, id):
        team = db.session.get(Team, id)

        if(team):
            db.session.delete(team)
            db.session.commit()
            response_body = {}
            return make_response(response_body, 204)
        else:
            response_body = {
                "error": "Team not found"
            }
            return make_response(response_body, 404)

api.add_resource(TeamByID, '/teams/<int:id>') 

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

if __name__ == '__main__':
    app.run(port=7777, debug=True)