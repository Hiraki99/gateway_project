from sqlalchemy import ForeignKey
from sqlalchemy import asc, desc, func
from sqlalchemy.sql.expression import and_, or_, exists
from sqlalchemy import Column, Integer, Unicode, String, DateTime, Boolean, Numeric, Text, Date, UniqueConstraint, UnicodeText, Index, Float
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
import json
import datetime
from . import Base, db_session
import uuid, random
from ..ulib import obj_to_dict


class BaseModel(object):
    __tablename__ = 'BaseModel'
    id = Column(Integer, primary_key=True)
    live = Column(Boolean,  nullable=False, default=True)
    createAt = Column(DateTime,   nullable=False, default=datetime.datetime.now, index=True)

    @staticmethod
    def to_dict(row):
        d = obj_to_dict(row)
        return d

    def __repr__(self):
        return '<%s is: id= %r>' % (self.__tablename__, self.id)


class ServerPreTrade(BaseModel, Base):
    __tablename__ = 'Account'

    id = Column(Integer, primary_key=True)

    host = Column(String(255), unique=True, nullable=False)
    port = Column(Integer,  nullable=False)
    national = Column(String(255),  nullable=False)
    type = Column(String(255),  nullable=False, index=True)
    live = Column(Boolean,  nullable=False, default=True) 
    currency = Column(String(255),  nullable=False, index=True)
    createAt = Column(DateTime,   nullable=False, default=datetime.datetime.now, index=True)

    def __init__(self, host, port, national, type, currency):
        self.host = host
        self.port = port
        self.national = national
        self.type = type
        self.currency = currency

    @staticmethod
    def get_all_server():
        with db_session() as session:
            list_query = session.query(ServerPreTrade).filter(
                ServerPreTrade.live == True).order_by(ServerPreTrade.createAt.desc())
            full_list_server = [ServerPreTrade.to_dict(row) for row in list_query]
        return full_list_server
    
    @staticmethod
    def get_server(server_id):
        with db_session() as session:
            list_query = session.query(ServerPreTrade).filter(ServerPreTrade.id == server_id,
                ServerPreTrade.live == True)
            full_server = [ServerPreTrade.to_dict(row) for row in list_query]
        return full_server
    