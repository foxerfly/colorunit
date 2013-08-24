import nose
#from colorunit import ColorUnit
import unittest
from my_module import check_value

class MyUnitTest(unittest.TestCase):
    def test_check_value_logs_warning(self):
        check_value({}, 'key')

    def test_Failed(self):
        self.assertEqual(1, 2)

    def test_Error(self):
        self.add()

    @unittest.skip("Skip test_skip")
    def test_skip(self):
        self.assertEqual(1, 2)

#if __name__ == '__main__':
#    nose.main(addplugins = [ColorUnit()])
