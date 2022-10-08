import unittest
from datetime import datetime

from pydate import is_before


class TestIsAfter(unittest.TestCase):
    def test_is_before_1(self):
        """
        returns true if the first date is after the second one
        :return:
        """
        self.assertTrue(is_before(datetime(1987, 1, 11), datetime(1989, 6, 10)))

    def test_is_before_2(self):
        """
        returns false if the first date is before the second one
        :return:
        """

        self.assertFalse(is_before(datetime(1989, 6, 11), datetime(1987, 1, 11)))

    def test_is_before_3(self):
        """
        returns false if the first date is equal to the second one
        :return:
        """

        self.assertFalse(is_before(datetime(1989, 6, 11), datetime(1989, 6, 11)))


if __name__ == "__main__":
    unittest.main()
