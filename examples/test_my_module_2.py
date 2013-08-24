import unittest
from my_module import divide

class MyUnitTest(unittest.TestCase):
    def test_add(self):
        divide(10, 0) #Deliberately
        
