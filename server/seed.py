#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Team, Player

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        User.query.delete()
        Team.query.delete()
        Player.query.delete()

        print("Starting seed...")
        user1 = User(name='Yuri', nationality='Haitian', age=26)
        user2 = User(name='Andrew', nationality='Mexican', age=21)
        user3 = User(name='Daniel', nationality='ST. Lucian', age=20)

        team1 = Team(team_name='YR', wins=23, draws=4, losses=8)
        team2 = Team(team_name='AV', wins=21, draws=5, losses=13)
        team3 = Team(team_name='DM', wins=19, draws=8, losses=4)

        # player1 = Player(player_name='CR7', position='LW', age=36, user_id=3, team_id=1),
        # player2 = Player(player_name='Kane', position='ST', age=32, user_id=2, team_id=2)
        # player3 = Player(player_name='Messi', position='RW', age=34, user_id=1, team_id=2)
        # player4 = Player(player_name='Neymar', position='LW', age=29, user_id=2, team_id=3)
        # player5 = Player(player_name='Mbappe', position='ST', age=26, user_id=3, team_id=3)
        # player6 = Player(player_name='Dembele', position='RW', age=23, user_id=2, team_id=3)
        # player7 = Player(player_name='Sane', position='LW', age=25, user_id=2, team_id=1)
        # player8 = Player(player_name='Mbappe', position='ST', age=26, user_id=3, team_id=3)
        # player9 = Player(player_name='Sterling', position='RW', age=31, user_id=1, team_id=2)
    
        db.session.add_all([user1, user2, user3])
        db.session.add_all([team1, team2, team3])
        # db.session.add_all([player1, player2, player3, player4, player5, player6])
        db.session.commit()
        print("Seeding completed")
