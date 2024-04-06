import unittest

from stats import * 
from math import add, double, square

class TestSquare(unittest.TestCase):
    def testingSquare(self):
        self.assertEqual(square(2), 4)
        self.assertNotEqual(square(4), 9)

class TestDouble(unittest.TestCase):
    def testingDouble(self):
        self.assertEqual(double(3), 6)
        self.assertEqual(double(10), 20)
        self.assertNotEqual(double(4), 9)

class TestAdd(unittest.TestCase):
    def testingAdd(self):
        self.assertEqual(add(20, 4), 24)
        self.assertEqual(add(2,2), 4)
        self.assertNotEqual(add(-3, 6), 9)

class TestMedian(unittest.TestCase):
    def testingMedian(self): 
        self.assertEqual(median([1,2,3]), 2)
        self.assertAlmostEqual(median([1,2,3,3,4,5,6,7]), 3.5, places=2)
        self.assertNotEqual(median([1,2,3]), 3)

class TestMean(unittest.TestCase):
    def testingMean(self): 
        self.assertEqual(mean([1,2,3,4]), 2.5)
        self.assertEqual(mean([2,2]),2)
        self.assertNotEqual(mean([2,3,4]), 5)

unittest.main()


