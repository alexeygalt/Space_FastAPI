from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Station(Base):
    """models to station object"""
    __tablename__ = 'station'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, unique=True, nullable=False)
    condition = sa.Column(sa.String, default='running')
    date_created = sa.Column(sa.DateTime, default=datetime.utcnow)
    date_broken = sa.Column(sa.DateTime)
    x = sa.Column(sa.Integer, default=100)
    y = sa.Column(sa.Integer, default=100)
    z = sa.Column(sa.Integer, default=100)


class Indication(Base):
    """models to indication object"""
    __tablename__ = 'indication'
    id = sa.Column(sa.Integer, primary_key=True)
    user = sa.Column(sa.String, nullable=False)
    axis = sa.Column(sa.String, nullable=False)
    distance = sa.Column(sa.Integer, nullable=False)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'))


class User(Base):
    __tablename__ = 'user'
    id = sa.Column(sa.Integer, primary_key=True)
    email = sa.Column(sa.Text, unique=True, nullable=False)
    username = sa.Column(sa.Text, unique=True, nullable=False)
    password_hash = sa.Column(sa.Text)
