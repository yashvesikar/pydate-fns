import unittest
from datetime import datetime

from pydate import add_months


class TestAddMonths(unittest.TestCase):
    def test_add_months_1(self) -> None:
        """
        adds the given number of months
        :return:
        """

        self.assertEqual(add_months(datetime(2014, 8, 1), 5), datetime(2015, 1, 1))

    def test_add_months_negative(self) -> None:
        """
        adds negative amount of months
        """
        self.assertEqual(add_months(datetime(2014, 8, 1), -5), datetime(2014, 3, 1))


if __name__ == "__main__":
    unittest.main()
