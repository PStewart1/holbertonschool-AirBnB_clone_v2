#!/usr/bin/python3
""""""
from sqlalchemy import create_engine, delete
from sqlalchemy.orm import sessionmaker
from os import getenv, environ
from models.base_model import Base


class DBStorage():
    """"""
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
        """"""
        self.__session = sessionmaker(bind=self.__engine)
        session = self.__session()
        # conn = self.__engine.connect()
        dics = {}
        if cls is None:
            itemlist = session.query().all()
        else:
            itemlist = session.query(cls).all()
        for item in itemlist:
            key = item.__class__.__name__ + "." + item.id
            dics.update({key: item})