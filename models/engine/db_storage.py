#!/usr/bin/python3
""" This module defines a class to manage a MySQL database """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base, BaseModel
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage():
    """ This class manages storage using a MySQL database, with SQLAlchemy """
    __engine = None
    __session = None

    def __init__(self):
        """ Starts the engine, and drops existing tables if in test env """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadate.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on the current database session all objects
        depending on the class name
        """
        classes = {
            'User': User, 'Place': Place,
            'State': State, 'City': City,
            'Review': Review, 'Amenity': Amenity
        }

        object_dict = {}

        if cls is not None:
            for obj in self.__session.query(cls).all():
                object_dict.update(
                    {'{}.{}'.format(type(cls).__name__, obj.id): obj})
        else:
            for name in classes.values():
                object_list = self.__session.query(name)
                for obj in object_list:
                    object_dict.update(
                        {'{}.{}'.format(type(obj).__name__, obj.id): obj})
        return object_dict

    def new(self, obj):
        """ add the object to the current database session """
        self.__session().add(obj)

    def save(self):
        """ commit all changes of the current database session  """
        self.__session().commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None """
        if obj is not None:
            self.__session().delete(obj)

    def reload(self):
        """ create all tables in the database """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)

    def close(self):
        """closes the current session"""
        self.__session.remove()
