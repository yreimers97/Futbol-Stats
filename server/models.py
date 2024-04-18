from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!

class City(db.Model, SerializerMixin):
    __tablename__ = 'cities'

    id = db.Column(db. Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    continent = db.Column(db.String, nullable=False)

    # my_users = db.relationship('User', back_populates='reviews' )

# class Review(db.Model):
#     __table__ = 'reviews'
#     id = db.Column(db.Integer, primary_key=True)
#     rating = db.Column(db.Integer)
#     text = db.Column(db.String)

#     review_id = db.Column(db.Integer, FOREIGNKEY='user.id')
#     reviews = db.relationship('Review', back_populates='my_users')