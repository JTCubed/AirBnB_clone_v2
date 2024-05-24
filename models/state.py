#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship, backref
import os
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)


    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref='state', cascade=
                              "all, delete, delete-orphan")
    else:
        @property
        def cities(self):
            """
            Returns the list of City instances with state_id equals to
            the current State.id
            """
            from model import storage
            cities_l = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities_l.append(city)
            return cities_l
