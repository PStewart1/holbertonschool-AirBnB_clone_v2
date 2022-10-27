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

    def test_create_city_file(self):
        """ creates new city """
        # os.environ['HBNB_TYPE_STORAGE'] = 'json'
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create City")
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all City")
            self.assertEqual('["[City]', f.getvalue()[:8])

    def test_create_user_file(self):
        """ creates new user """
        # os.environ['HBNB_TYPE_STORAGE'] = 'json'
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all User")
            self.assertEqual('["[User]', f.getvalue()[:8])

    def test_show_state_file(self):
        """ creates new user """
        # os.environ['HBNB_TYPE_STORAGE'] = 'json'
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create State")
            state_id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show State " + state_id)
            self.assertEqual('[State]', f.getvalue()[:7])

    def test_create_state_db(self):
        """ creates new state """
        os.environ['HBNB_TYPE_STORAGE'] = 'db'
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create State")
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all State")
            self.assertEqual('["[State]', f.getvalue()[:9])
