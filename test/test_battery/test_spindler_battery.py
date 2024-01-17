from battery.spindler_battery import spindler_battery
import unittest
from datetime import date

class test_spindler_battery(unittest.TestCase):
    def test_needs_service(self):
        last_service_date = date(2016, 12, 18)
        current_date = date.today()
        battery = spindler_battery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_doesnt_need_service(self):
        last_service_date = date(2023, 12, 18)
        current_date = date.today()
        battery = spindler_battery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())
