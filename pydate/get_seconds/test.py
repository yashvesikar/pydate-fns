import math
import unittest
from datetime import datetime

from pydate import get_seconds


class TestGetSeconds(unittest.TestCase):
    def test_returns_seconds(self) -> None:
        """returns the seconds"""
        result = get_seconds(datetime(2012, 2, 29, 11, 45, 5, 123000))
        self.assertEqual(result, 5)

    def test_accepts_timestamp(self) -> None:
        """accepts a timestamp"""
        result = get_seconds(datetime(2012, 2, 29, 11, 45, 5, 123000).timestamp())
        self.assertEqual(result, 5)

    def test_returns_nan_for_invalid_date(self) -> None:
        """returns NaN if the given date is invalid"""
        result = get_seconds(float('nan'))
        self.assertTrue(math.isnan(result))


if __name__ == "__main__":
    unittest.main()