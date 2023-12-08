# application/unit_tests/test_weather_functions.py
import unittest
import sys
sys.path.insert(0, "../application")

from database.weather_db import (
    create_weather_station,
    get_all_weather_stations,
    create_weather_data,
    get_weather_data_for_station,
)

class WeatherFunctionsTestCase(unittest.TestCase):

    def test_create_weather_station(self):
        # Your test code for creating a weather station
        create_weather_station(
            name='Test Station', 
            mac_address='00:00:00:00:00:02', 
            address='456 Main St, City, Country'
            )
        stations = get_all_weather_stations()
        self.assertEqual(len(stations), 1)

    def test_create_weather_data(self):
        # Your test code for creating weather data
        create_weather_data(mac_address='00:00:00:00:00:02', tempf=75.5, humidity=50)
        data = get_weather_data_for_station(mac_address='00:00:00:00:00:02')
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0].tempf, 75.5)

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
