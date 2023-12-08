from .sql_base import Base

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker


class WeatherStation(Base):
    __tablename__ = 'WeatherStation'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    macAddress = Column(String(17), unique=True, nullable=False)
    address = Column(String(255))
    latitude = Column(Float)
    longitude = Column(Float)
    elevation = Column(Float)
    location = Column(String(255))
