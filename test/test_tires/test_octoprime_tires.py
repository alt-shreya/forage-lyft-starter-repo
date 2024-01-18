import unittest
from tires.octoprime_tires import octoprime_tires

class test_octoprime_tires(unittest.TestCase):
    def test_needs_service(self):
        tires = octoprime_tires([0.9, 1, 1, 1])
        self.assertTrue(tires.needs_service())
    
    def test_doesnt_need_service(self):
        tires = octoprime_tires([0.9, 0.1, 0.2, 0.1])
        self.assertFalse(tires.needs_service())