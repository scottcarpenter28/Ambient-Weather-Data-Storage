from .sql_base import Base
from .weather_station import WeatherStation

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

class WeatherData(Base):
    __tablename__ = 'WeatherData'

    id = Column(Integer, primary_key=True, autoincrement=True)
    macAddress = Column(String(17), ForeignKey('WeatherStation.macAddress'), nullable=False)
    baromabsin = Column(Float)
    baromrelin = Column(Float)
    battin = Column(Integer)
    battout = Column(Integer)
    dailyrainin = Column(Float)
    date = Column(DateTime)
    dateutc = Column(Integer)
    dewPoint = Column(Float)
    dewPointin = Column(Float)
    eventrainin = Column(Float)
    feelsLike = Column(Float)
    feelsLikein = Column(Float)
    hourlyrainin = Column(Float)
    humidity = Column(Integer)
    humidityin = Column(Integer)
    lastRain = Column(DateTime)
    maxdailygust = Column(Float)
    monthlyrainin = Column(Float)
    solarradiation = Column(Float)
    tempf = Column(Float)
    tempinf = Column(Float)
    uv = Column(Integer)
    weeklyrainin = Column(Float)
    winddir = Column(Integer)
    winddir_avg10m = Column(Integer)
    windgustmph = Column(Float)
    windspdmph_avg10m = Column(Float)
    windspeedmph = Column(Float)
    yearlyrainin = Column(Float)

    station = relationship('WeatherStation', back_populates='data')
