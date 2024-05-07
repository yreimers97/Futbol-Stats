#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, League, Team, Player

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        League.query.delete()
        Team.query.delete()
        Player.query.delete()

        print("Starting seed...")
        league1 = League(league_name='Barclays', country='England')
        league2 = League(league_name='La Liga', country='Spain')
        league3 = League(league_name='Bundesliga', country='Germany')
        league4 = League(league_name='Serie A', country='Italy')
        league5 = League(league_name='Ligue 1', country='France')

        team1 = Team(team_name='Real Madrid', wins=23, draws=4, losses=8)
        team2 = Team(team_name='Barcelona', wins=21, draws=5, losses=13)
        team3 = Team(team_name='Bayern Munich', wins=19, draws=8, losses=4)

        player1 = Player(player_name='Messi', goals=25, assists=9, league_id=2, team_id=2)
        player2 = Player(player_name='CR7', goals=21, assists=6, league_id=1)
        player3 = Player(player_name='Sane', goals=19, assists=12, league_id=3, team_id=3)
    
        db.session.add_all([league1, league2, league3, league4, league5])
        db.session.all_all([team1, team2, team3])
        db.session.all_all([player1, player2, player3])
        db.session.commit()
        print("Seeding completed")
