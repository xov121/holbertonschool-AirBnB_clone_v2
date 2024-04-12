import models
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")

    else:
        @property
        def cities(self):
            """Get a list of all related City objects."""
            from models.city import City
            city_list = models.storage.all(City).values()
            return [city for city in city_list if city.state_id == self.id]
