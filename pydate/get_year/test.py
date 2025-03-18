import math
import unittest
from datetime import datetime

from pydate import get_year


class TestGetYear(unittest.TestCase):
    def test_returns_year(self) -> None:
        """returns the year"""
        result = get_year(datetime(2014, 7, 2))
        self.assertEqual(result, 2014)

    def test_accepts_timestamp(self) -> None:
        """accepts a timestamp"""
        result = get_year(datetime(2014, 7, 2).timestamp())
        self.assertEqual(result, 2014)

    def test_returns_nan_for_invalid_date(self) -> None:
        """returns NaN if the given date is invalid"""
        result = get_year(float('nan'))
        self.assertTrue(math.isnan(result))


if __name__ == "__main__":
    unittest.main()