import math
import unittest
from datetime import datetime

from pydate import get_milliseconds


class TestGetMilliseconds(unittest.TestCase):
    def test_returns_milliseconds(self) -> None:
        """returns the milliseconds"""
        result = get_milliseconds(datetime(2012, 2, 29, 11, 45, 5, 123000))
        self.assertEqual(result, 123)

    def test_accepts_timestamp(self) -> None:
        """accepts a timestamp"""
        # Note: Timestamps might lose some precision with milliseconds
        result = get_milliseconds(datetime(2012, 2, 29, 11, 45, 5, 123000).timestamp())
        self.assertEqual(result, 123)

    def test_returns_nan_for_invalid_date(self) -> None:
        """returns NaN if the given date is invalid"""
        result = get_milliseconds(float('nan'))
        self.assertTrue(math.isnan(result))


if __name__ == "__main__":
    unittest.main()