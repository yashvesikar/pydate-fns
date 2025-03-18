import math
import unittest
from datetime import datetime

from pydate import get_hours


class TestGetHours(unittest.TestCase):
    def test_returns_hours(self) -> None:
        """returns the hours"""
        result = get_hours(datetime(2012, 2, 29, 11, 45))
        self.assertEqual(result, 11)

    def test_accepts_timestamp(self) -> None:
        """accepts a timestamp"""
        result = get_hours(datetime(2012, 2, 29, 11, 45).timestamp())
        self.assertEqual(result, 11)

    def test_returns_nan_for_invalid_date(self) -> None:
        """returns NaN if the given date is invalid"""
        result = get_hours(float('nan'))
        self.assertTrue(math.isnan(result))


if __name__ == "__main__":
    unittest.main()