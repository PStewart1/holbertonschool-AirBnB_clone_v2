#!/usr/bin/python3
""" This module defines a class to manage a MySQL database """
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base, BaseModel


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
        depending of the class name
        """
        # from models.city import City
        # from models.state import State
        # from sqlalchemy.orm import aliased
        # self.__session = sessionmaker(bind=self.__engine)
        # session = self.__session()
        # conn = self.__engine.connect()
        dics = {}
        # classname = aliased(cls)
        if cls is None:
            itemlist = self.__session.query().all()
        else:
            itemlist = self.__session.query(cls).all()
        for item in itemlist:
            key = item.__class__.__name__ + "." + item.id
            delattr(item, '_sa_instance_state')
            # if '_sa_instance_state' in item.keys():
            #     item.pop('_sa_instance_state')
            dics.update({key: item})
        return dics

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
        from models.city import City
        from models.state import State
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)
