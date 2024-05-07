from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

class League(db.Model, SerializerMixin):
    __tablename__ = 'leagues'

    id = db.Column(db.Integer, primary_key=True)
    league_name = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)

    players = db.relationship('Player', back_populates='league', cascade='all')

    teams = association_proxy('players', 'team', creator = lambda t: Player(team = t))

class Team(db.Model, SerializerMixin):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String, nullable=False)
    wins = db.Column(db.Integer, nullable=False)
    draws = db.Column(db.Integer, nullable=False)
    losses = db.Column(db.Integer, nullable=False)

    players = db.relationship('Player', back_populates='team', cascade='all')

    leagues = association_proxy('players', 'league', creator = lambda l: Player(league = l))

class Player(db.Model, SerializerMixin):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String)
    position = db.Column
    goals = db.Column(db.Integer, nullable=False)
    assists = db.Column(db.Integer, nullable=False)

    league_id = db.Column(db.Integer, db.ForeignKey('leagues.id'))
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))

    league = db.relationship('League', back_populates='players')
    team = db.relationship('Team', back_populates='players')

# class Follower(db.Model, SerializerMixin):
#     __tablename__ = 'followers'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String, nullable=False)
#     country = db.Column(db.String, nullable=False)
#     city = db.Column(db.String, nullable=False)

# class City(db.Model, SerializerMixin):
#     __tablename__ = 'cities'

#     id = db.Column(db. Integer, primary_key=True)
#     name = db.Column(db.String, nullable=False)
#     country = db.Column(db.String, nullable=False)
#     continent = db.Column(db.String, nullable=False)
    
    # people = db.relationship('Person', back_populates='city', cascade='all')
    # activity = db.relationship('Activity', back_populates='cities' )

# class Activity(db.Model, SerializerMixin):
#     __tablename__ = 'activities'
#     id = db.Column(db.Integer, primary_key=True)
#     fav_food = db.Column(db.String)
#     fav_drink = db.Column(db.String)
#     excursion = db.Column(db.String)

#     activity_id = db.Column(db.Integer, db.ForeignKey('cities.id'))

#     # city = db.relationship('City', back_populates='activities')

# class Person(db.Model, SerializerMixin):
#     __tablename__ = 'people'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     salary = db.Column(db.Float, nullable=False)

#     city_id = db.Column(db.Integer, db.ForeignKey('people.id'))
#     city = db.relationship('City', back_populates='people')