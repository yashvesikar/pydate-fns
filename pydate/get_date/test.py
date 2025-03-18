import math
import unittest
from datetime import datetime

from pydate import get_date


class TestGetDate(unittest.TestCase):
    def test_returns_day_of_month(self) -> None:
        """returns the day of the month"""
        result = get_date(datetime(2012, 2, 29))
        self.assertEqual(result, 29)

    def test_accepts_timestamp(self) -> None:
        """accepts a timestamp"""
        result = get_date(datetime(2012, 2, 29).timestamp())
        self.assertEqual(result, 29)

    def test_returns_nan_for_invalid_date(self) -> None:
        """returns NaN if the given date is invalid"""
        result = get_date(float('nan'))
        self.assertTrue(math.isnan(result))


if __name__ == "__main__":
    unittest.main()