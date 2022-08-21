import unittest
from datetime import datetime

from core.add_days.add_days import add_days


class TestAddDays(unittest.TestCase):
    def test_add_days_1(self):
        """
        adds the given number of days
        :return:
        """
        self.assertEqual(add_days(datetime(2014, 8, 1), 10), datetime(2014, 8, 11))


if __name__ == "__main__":
    unittest.main()
