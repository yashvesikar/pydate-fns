from audioop import add
import unittest
from datetime import datetime

from pydate import add_months


class TestAddMonths(unittest.TestCase):
    def test_add_months_1(self):
        """
        adds the given number of months
        :return:
        """

        self.assertEqual(add_months(datetime(2014, 8, 1), 5), datetime(2015, 1, 1))


if __name__ == "__main__":
    unittest.main()
