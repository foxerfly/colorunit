import unittest
from my_module import check_value

class MyUnitTest(unittest.TestCase):
    def test_check_value_logs_warning(self):
        check_value({}, 'key')
