# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package
import datetime
import unittest

from src.core import add

class TestSimple(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(datetime.datetime(2019, 1, 1), {"weeks": 1}), datetime.datetime(2019, 1, 8))


if __name__ == '__main__':
    unittest.main()
