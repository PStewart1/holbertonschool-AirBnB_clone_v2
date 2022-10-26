#!/usr/bin/python3
""" module containing tests for State class """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ tests for State class """

    # def __init__(self, *args, **kwargs):
    #     """ creates new instance of State object """
    #     super().__init__(*args, **kwargs)
    #     self.name = "State"
    #     self.value = State

    def test_name3(self):
        """ tests that name attribute is string """
        new = State()
        new.name = 'Texas'
        self.assertEqual(type(new.name), str)
