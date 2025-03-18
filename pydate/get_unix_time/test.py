import math
import unittest
from datetime import datetime, timezone

from pydate import get_unix_time


class TestGetUnixTime(unittest.TestCase):
    def test_returns_unix_timestamp(self) -> None:
        """returns the Unix timestamp (seconds)"""
        # Use UTC to ensure consistent timestamps
        dt = datetime(2012, 2, 29, 11, 45, 5, tzinfo=timezone.utc)
        result = get_unix_time(dt)
        self.assertEqual(result, 1330515905)

    def test_accepts_timestamp(self) -> None:
        """accepts a timestamp"""
        # Use UTC to ensure consistent timestamps
        dt = datetime(2012, 2, 29, 11, 45, 5, tzinfo=timezone.utc)
        result = get_unix_time(dt.timestamp())
        self.assertEqual(result, 1330515905)

    def test_returns_nan_for_invalid_date(self) -> None:
        """returns NaN if the given date is invalid"""
        result = get_unix_time(float('nan'))
        self.assertTrue(math.isnan(result))


if __name__ == "__main__":
    unittest.main()