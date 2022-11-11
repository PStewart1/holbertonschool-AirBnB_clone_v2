#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table(
    'place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True),
    Column('amenity_id', String(60), ForeignKey('amenities.id'),
           primary_key=True)
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
            'Review', backref='place', cascade="all, delete, delete-orphan")
        amenities = relationship(
            "Amenity", secondary=place_amenity,
            back_populates='place_amenities', viewonly=False)

    else:
        @property
        def reviews(self):
            from models import storage, review
            dics = storage.all(review.Review)
            diclist = []
            for v in dics.values():
                if v.place_id == self.id:
                    diclist.append(v)
            return diclist

        @property
        def amenities(self):
            from models import storage, amenity
            dics = storage.all(amenity.Amenity)
            id_list = self.amenity_ids
            diclist = []
            for v in dics.values():
                if v.id in id_list:
                    diclist.append(v)
            return diclist

        @amenities.setter
        def amenities(self, obj):
            if obj.__class__.__name__ == 'Amenity':
                self.amenity_ids.append(obj.id)
