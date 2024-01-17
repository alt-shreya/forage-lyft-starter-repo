import unittest
import random

from engine.capulet_engine import CapuletEngine


class TestCapuletEngine(unittest.TestCase):
    def test_needs_service(self):
        current_mileage = 30002
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())
    
    def test_doesnt_need_service(self):
        current_mileage = random.randint(0,29999)
        last_service_mileage = random.randint(0,29999)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())