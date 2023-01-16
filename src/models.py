import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    
    id_user = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)
    email= Column(String(50), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
   
    id_characters = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)

class Planets(Base):
    __tablename__= 'planets'

    id_planets = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)

class Fav_Characters(Base):
    __tablename__= 'fav_characters' 

    id_fav_characters = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id_user'))
    id_characters = Column(Integer, ForeignKey('characters.id_characters'))

class Fav_Planets(Base):
    __tablename__= 'fav_planets'

    id_fav_planets = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id_user'))
    id_planets = Column(Integer, ForeignKey('planets.id_planets'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
