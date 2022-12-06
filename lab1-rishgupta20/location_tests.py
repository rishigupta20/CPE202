import unittest
from location import *


class TestLab1(unittest.TestCase):

    def test_init(self):
        loc1 = Location('SLO', 35.3, -120.7)
        self.assertEqual(loc1.name, 'SLO')
        self.assertEqual(loc1.lat, 35.3)
        self.assertEqual(loc1.lon, -120.7)
        self.assertNotEqual(loc1.name, 'sLO')
        loc2 = Location('France', 46.2, 2.2)
        self.assertEqual(loc2.name, 'France')
        self.assertEqual(loc2.lat, 46.2)
        self.assertEqual(loc2.lon, 2.2)
        self.assertNotEqual(loc2.lon, 1.9)
        loc3 = loc1
        self.assertEqual(loc3.name, 'SLO')
        self.assertEqual(loc3.lat, 35.3)
        self.assertEqual(loc3.lon, -120.7)
        self.assertNotEqual(loc3.lon, -120.1)
        loc4 = Location('Barcelona', 41.4, 2.2)
        self.assertEqual(loc4.name, 'Barcelona')
        self.assertEqual(loc4.lat, 41.4)
        self.assertEqual(loc4.lon, 2.2)

    def test_eq(self):
        loc1 = Location('SLO', 35.3, -120.7)
        loc2 = Location('SLO', 35.3, -120.7)
        loc3 = Location('Paris', 48.9, 2.4)
        loc4 = Location('Barcelona', 41.4, 2.2)
        loc5 = Location('India', 20.6, 79)
        loc6 = Location('India', 20.6, 79)
        loc7 = Location('India', 20.6, 80)
        self.assertEqual(loc1, loc2)
        self.assertNotEqual(loc3, loc4)
        self.assertEqual(loc5, loc6)
        self.assertNotEqual(loc6, loc7)
        self.assertNotEqual(loc5, Location(54, 68, 20))

    def test_repr(self):
        loc1 = Location('SLO', 35.3, -120.7)
        self.assertEqual(repr(loc1), "Location('SLO', 35.3, -120.7)")
        self.assertNotEqual(repr(loc1), "Location('SPO', 35.3, -120.7)")
        loc2 = Location('India', 20.6, 79)
        self.assertEqual(repr(loc2), "Location('India', 20.6, 79)")
        self.assertNotEqual(repr(loc2), "Location('India', 20.9, 81)")
        loc3 = Location('Barcelona', 41.4, 2.2)
        self.assertEqual(repr(loc3), "Location('Barcelona', 41.4, 2.2)")
        self.assertNotEqual(repr(loc3), "Location('Barcelona', 41.9, 2.2)")


if __name__ == "__main__":
    unittest.main()
