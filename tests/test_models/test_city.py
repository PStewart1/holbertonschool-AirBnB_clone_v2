#!/usr/bin/python3
""" module containing tests for City class"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ tests for City class """

    def __init__(self, *args, **kwargs):
        """ creates new instance of City object """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    # def test_state_id(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.state_id), str)

    # def test_name(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.name), str)
