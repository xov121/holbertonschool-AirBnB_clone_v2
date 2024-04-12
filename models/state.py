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


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")


@property
def cities(self):
    """Get a list of all related City objects."""
    from models import storage
    from models.city import City
    city_list = [
        city for city in storage.all(City).values()
        if city.state_id == self.id
    ]
    return city_list
