import math
import unittest
from datetime import datetime

from pydate import get_month


class TestGetMonth(unittest.TestCase):
    def test_returns_month(self) -> None:
        """returns the month (1-12)"""
        result = get_month(datetime(2012, 2, 29))
        self.assertEqual(result, 2)  # February is 2

    def test_accepts_timestamp(self) -> None:
        """accepts a timestamp"""
        result = get_month(datetime(2012, 2, 29).timestamp())
        self.assertEqual(result, 2)  # February is 2

    def test_returns_nan_for_invalid_date(self) -> None:
        """returns NaN if the given date is invalid"""
        result = get_month(float('nan'))
        self.assertTrue(math.isnan(result))


if __name__ == "__main__":
    unittest.main()