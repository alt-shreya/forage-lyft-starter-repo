import unittest
from engine.sternman_engine import SternmanEngine 

class TestSternmanEngine(unittest.TestCase):
    def test_needs_service(self):
        warning_light_status = True
        engine = SternmanEngine(warning_light_status)
        self.assertTrue(engine.needs_service())

    def test_doesnt_need_service(self):
        warning_light_status = False
        engine = SternmanEngine(warning_light_status)
        self.assertFalse(engine.needs_service())