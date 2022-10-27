#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    # def __init__(self, *args, **kwargs):
    #     """ """
    #     super().__init__(*args, **kwargs)
    #     self.name = "Place"
    #     self.value = Place

    def test_city_id(self):
        """ """
        new = Place()
        new.city_id = '1'
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = Place()
        new.user_id = '1'
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = Place()
        new.name = 'Alberquerqe'
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = Place()
        new.description = 'I. HATE. SOURKRAUT!'
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = Place()
        new.number_rooms = 11
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = Place()
        new.number_bathrooms = 0
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = Place()
        new.max_guest = 5000
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = Place()
        new.price_by_night = 50
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = Place()
        new.latitude = 9.9
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = Place()
        new.longitude = 5.5
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """ """
        new = Place()
        self.assertEqual(type(new.amenity_ids), list)
