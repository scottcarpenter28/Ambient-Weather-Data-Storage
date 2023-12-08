from datetime import datetime
from typing import List

from .db_config import (
    DATABASE_ENGINE,
    DATABASE_ECHO
)
from tables.sql_base import Base
from tables.weather_data import WeatherData
from tables.weather_station import WeatherStation

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(DATABASE_ENGINE, echo=DATABASE_ECHO)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


def create_weather_station(
        name: str, 
        mac_address: str, 
        address: str | None = None, 
        latitude: float | None = None, 
        longitude: float | None = None, 
        elevation: float | None=None, 
        location: str = None
    ) -> None:
    """
    Inserts a new weather station into the database.
    :param name: The name of the weather station.
    :param mac_address: The unique mac address.
    :param address: The physical address of the weather station. 
    :param latitude: The latitude coordinate of the weather station.
    :param longitude: The longitude coordinate of the weather station.
    :param elevation: The elevation of the weather station.
    :param location: The location of the weather station.
    """
    new_station = WeatherStation(
        name=name,
        macAddress=mac_address,
        address=address,
        latitude=latitude,
        longitude=longitude,
        elevation=elevation,
        location=location
    )

    session.add(new_station)
    session.commit()
    session.close()


def get_all_weather_stations() -> List[WeatherStation]:
    """
    Gets a list of all weather stations in the database.
    :return: A list of weather station objects.
    """
    stations = session.query(WeatherStation).all()
    session.close()
    return stations


def create_weather_data(
        mac_address: str, 
        baromabsin: float,
        baromrelin: float,
        battin: int,
        battout: int,
        dailyrainin: float,
        date: datetime,
        dateutc: float,
        dewPoint: float,
        dewPointin: float,
        eventrainin: float,
        feelsLike: float,
        feelsLikein: float,
        hourlyrainin: float,
        humidity: float,
        humidityin: float,
        lastRain: datetime,
        maxdailygust: float,
        monthlyrainin: float,
        solarradiation: float,
        tempf: float,
        tempinf: float,
        uv: float,
        weeklyrainin: float,
        winddir: int,
        winddir_avg10m: int,
        windgustmph: float,
        windspdmph_avg10m: float,
        windspeedmph: float,
        yearlyrainin: float,
    ) -> None:
    """
    Inserts a new weather datapoint into the database.
    :param mac_address: The mac address of the weather station that recorded the data.
    :param baromabsin:
    :param baromrelin:
    :param battin:
    :param battout:
    :param dailyrainin:
    :param date:
    :param dateutc:
    :param dewPoint:
    :param dewPointin:
    :param eventrainin:
    :param feelsLike:
    :param feelsLikein:
    :param hourlyrainin:
    :param humidity:
    :param humidityin:
    :param lastRain:
    :param maxdailygust:
    :param monthlyrainin:
    :param solarradiation:
    :param tempf:
    :param tempinf:
    :param uv:
    :param weeklyrainin:
    :param winddir:
    :param winddir_avg10m:
    :param windgustmph:
    :param windspdmph_avg10m:
    :param windspeedmph:
    :param yearlyrainin:
    :return: None
    """
    new_data = WeatherData(
        macAddress=mac_address,
        baromabsin=baromabsin,
        baromrelin=baromrelin,
        battin=battin,
        battout=battout,
        dailyrainin=dailyrainin,
        date=date,
        dateutc=dateutc,
        dewPoint=dewPoint,
        dewPointin=dewPointin,
        eventrainin=eventrainin,
        feelsLike=feelsLike,
        feelsLikein=feelsLikein,
        hourlyrainin=hourlyrainin,
        humidity=humidity,
        humidityin=humidityin,
        lastRain=lastRain,
        maxdailygust=maxdailygust,
        monthlyrainin=monthlyrainin,
        solarradiation=solarradiation,
        tempf=tempf,
        tempinf=tempinf,
        uv=uv,
        weeklyrainin=weeklyrainin,
        winddir=winddir,
        winddir_avg10m=winddir_avg10m,
        windgustmph=windgustmph,
        windspdmph_avg10m=windspdmph_avg10m,
        windspeedmph=windspeedmph,
        yearlyrainin=yearlyrainin,
    )

    session.add(new_data)
    session.commit()
    session.close()


def get_weather_data_for_station(mac_address) -> List[WeatherData]:
    """
    Gets a list of all weather data recorded for a weather station.
    :param mac_address: The unique mac address to search for.
    :return : A list of all recorded weather data.
    """
    data = session.query(WeatherData).filter_by(macAddress=mac_address).all()
    session.close()
    return data