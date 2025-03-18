import math
import unittest
from datetime import datetime

from pydate import get_minutes


class TestGetMinutes(unittest.TestCase):
    def test_returns_minutes(self) -> None:
        """returns the minutes"""
        result = get_minutes(datetime(2012, 2, 29, 11, 45, 5))
        self.assertEqual(result, 45)

    def test_accepts_timestamp(self) -> None:
        """accepts a timestamp"""
        result = get_minutes(datetime(2012, 2, 29, 11, 45, 5).timestamp())
        self.assertEqual(result, 45)

    def test_returns_nan_for_invalid_date(self) -> None:
        """returns NaN if the given date is invalid"""
        result = get_minutes(float('nan'))
        self.assertTrue(math.isnan(result))


if __name__ == "__main__":
    unittest.main()