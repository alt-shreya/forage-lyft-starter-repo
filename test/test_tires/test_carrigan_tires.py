import unittest
from tires.carrigan_tires import carrigan_tires

class test_carrigan_tires(unittest.TestCase):
    def test_needs_service(self):
        tires = carrigan_tires([0.9, 0.1, 0.3, 0.6])
        self.assertTrue(tires.needs_service())
    
    def test_doesnt_need_service(self):
        tires = carrigan_tires([0.2, 0.1, 0.3, 0.6])
        self.assertFalse(tires.needs_service())
