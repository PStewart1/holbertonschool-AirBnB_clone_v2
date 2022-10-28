#!/usr/bin/python3
""" Module for testing the console"""
import unittest
from unittest.mock import patch
from io import StringIO
# from models.base_model import BaseModel
# from models import storage
from console import HBNBCommand
import os


class test_console(unittest.TestCase):
    """ Class to test the console """

    # def setUp(self):
    #     """ Set up test environment """
    #     os.environ['HBNB_ENV'] = 'test'
    @classmethod
    def setUpClass(cls):
        """setup for the test"""
        os.environ['HBNB_ENV'] = 'test'
        cls.consol = HBNBCommand()

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.consol

    def tearDown(self):
        """Remove temporary file (file.json) created as a result"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_emptyline(self):
        """ tests empty line input """
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("\n")
            self.assertEqual('', f.getvalue())

    def test_create_state_file(self):
        """ creates new state """
        os.environ['HBNB_TYPE_STORAGE'] = 'json'
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create State")
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all State")
            self.assertEqual('["[State]', f.getvalue()[:9])

    def test_create_Texas_file(self):
        """ creates new state """
        os.environ['HBNB_TYPE_STORAGE'] = 'json'
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create State name='Texas'")
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all State")
            self.assertEqual('["[State]', f.getvalue()[:9])

    def test_create_city_file(self):
        """ creates new city """
        os.environ['HBNB_TYPE_STORAGE'] = 'json'
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create City")
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all City")
            self.assertEqual('["[City]', f.getvalue()[:8])

    def test_create_user_file(self):
        """ creates new user """
        os.environ['HBNB_TYPE_STORAGE'] = 'json'
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all User")
            self.assertEqual('["[User]', f.getvalue()[:8])

    def test_create_place_file(self):
        """ creates new place """
        os.environ['HBNB_TYPE_STORAGE'] = 'json'
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create Place")
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all Place")
            self.assertEqual('["[Place]', f.getvalue()[:9])

    def test_create_review_file(self):
        """ creates new user """
        os.environ['HBNB_TYPE_STORAGE'] = 'json'
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create Review")
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all Review")
            self.assertEqual('["[Review]', f.getvalue()[:10])

    def test_create_amenity_file(self):
        """ creates new user """
        os.environ['HBNB_TYPE_STORAGE'] = 'json'
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create Amenity")
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all Amenity")
            self.assertEqual('["[Amenity]', f.getvalue()[:11])

    def test_show_state_file(self):
        """ creates new user """
        os.environ['HBNB_TYPE_STORAGE'] = 'json'
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create State")
            state_id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show State " + state_id)
            self.assertEqual('[State]', f.getvalue()[:7])

    def test_count_state_file(self):
        """ creates new user """
        os.environ['HBNB_TYPE_STORAGE'] = 'json'
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("count State")
            state_num = int(f.getvalue()[:1])
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create State")
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("count State")
            self.consol.onecmd("count State")
            self.assertEqual(str(state_num + 1), f.getvalue()[:1])

    def test_destroy_state_file(self):
        """ creates new user """
        os.environ['HBNB_TYPE_STORAGE'] = 'json'
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("count State")
            state_num = int(f.getvalue()[:1])
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create State")
            state_id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("count State")
            self.assertEqual(str(state_num + 1), f.getvalue()[:1])
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("destroy State " + state_id)
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("count State")
            self.assertEqual(str(state_num), f.getvalue()[:1])

    def test_create_state_db(self):
        """ creates new state, using db """
        os.environ['HBNB_TYPE_STORAGE'] = 'db'
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create State")
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all State")
            self.assertEqual('["[State]', f.getvalue()[:9])

    def test_create_Texas_db(self):
        """ creates new state, using db """
        os.environ['HBNB_TYPE_STORAGE'] = 'db'
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create State name='Texas'")
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all State")
            self.assertEqual('["[State]', f.getvalue()[:9])

    def test_create_city_db(self):
        """ creates new city, using db """
        os.environ['HBNB_TYPE_STORAGE'] = 'db'
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create City")
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all City")
            self.assertEqual('["[City]', f.getvalue()[:8])

    def test_create_user_db(self):
        """ creates new user, using db """
        os.environ['HBNB_TYPE_STORAGE'] = 'db'
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all User")
            self.assertEqual('["[User]', f.getvalue()[:8])

    def test_create_place_db(self):
        """ creates new place, using db """
        os.environ['HBNB_TYPE_STORAGE'] = 'db'
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create Place")
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all Place")
            self.assertEqual('["[Place]', f.getvalue()[:9])

    def test_create_review_db(self):
        """ creates new review, using db """
        os.environ['HBNB_TYPE_STORAGE'] = 'db'
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create Review")
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all Review")
            self.assertEqual('["[Review]', f.getvalue()[:10])

    def test_create_amenity_db(self):
        """ creates new amenity, using db """
        os.environ['HBNB_TYPE_STORAGE'] = 'db'
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create Amenity")
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all Amenity")
            self.assertEqual('["[Amenity]', f.getvalue()[:11])

    def test_show_state_db(self):
        """ show new state """
        os.environ['HBNB_TYPE_STORAGE'] = 'db'
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create State")
            state_id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show State " + state_id)
            self.assertEqual('[State]', f.getvalue()[:7])

    def test_count_state_db(self):
        """ counts states, using db """
        os.environ['HBNB_TYPE_STORAGE'] = 'db'
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("count State")
            state_num = int(f.getvalue()[:1])
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create State")
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("count State")
            self.consol.onecmd("count State")
            self.assertEqual(str(state_num + 1), f.getvalue()[:1])

    def test_destroy_state_db(self):
        """ deletes new state, using db"""
        os.environ['HBNB_TYPE_STORAGE'] = 'db'
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("count State")
            state_num = int(f.getvalue()[:1])
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create State")
            state_id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("count State")
            self.assertEqual(str(state_num + 1), f.getvalue()[:1])
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("destroy State " + state_id)
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("count State")
            self.assertEqual(str(state_num), f.getvalue()[:1])
