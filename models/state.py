#!/usr/bin/python3
""" State Module for HBNB project
with a class State that inherits from BaseModel
and a class attribute name that represents the
 state name with a string (128)"""
import models
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.engine.db_storage import DBStorage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    @property
    def cities(self):
        city_list = []
        for city in list(models.storage.all(City).values()):
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
