from engine.willoughby_engine import WilloughbyEngine
import unittest
from random import randint

class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_doesnt_need_service(self):
        current_mileage = randint(0,59999)
        last_service_mileage = randint(0,59999)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

