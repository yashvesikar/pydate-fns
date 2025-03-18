import math
import unittest
from datetime import datetime, timezone

from pydate import difference_in_milliseconds


class TestDifferenceInMilliseconds(unittest.TestCase):
    def test_returns_number_of_milliseconds_between_dates(self) -> None:
        """returns the number of milliseconds between dates"""
        result = difference_in_milliseconds(
            datetime(2014, 7, 2, 12, 30, 21, 700000),  # Jul 2 2014, 12:30:21.700
            datetime(2014, 7, 2, 12, 30, 20, 600000)   # Jul 2 2014, 12:30:20.600
        )
        self.assertEqual(result, 1100.0)

    def test_returns_negative_for_earlier_later_date(self) -> None:
        """returns negative number if the first date is before the second"""
        result = difference_in_milliseconds(
            datetime(2014, 7, 2, 12, 30, 20, 600000),  # Jul 2 2014, 12:30:20.600
            datetime(2014, 7, 2, 12, 30, 21, 700000)   # Jul 2 2014, 12:30:21.700
        )
        self.assertEqual(result, -1100.0)

    def test_accepts_timestamps(self) -> None:
        """accepts timestamps"""
        early = datetime(2014, 8, 11, 0, 0, tzinfo=timezone.utc)
        late = datetime(2014, 8, 11, 0, 0, 0, 123000, tzinfo=timezone.utc)
        result = difference_in_milliseconds(late.timestamp(), early.timestamp())
        self.assertEqual(result, 123.0)

    def test_returns_0_if_dates_are_equal(self) -> None:
        """returns 0 if the dates are equal"""
        date = datetime(2014, 8, 5, 0, 0)
        result = difference_in_milliseconds(date, date)
        self.assertEqual(result, 0)

    def test_returns_nan_if_first_date_is_invalid(self) -> None:
        """returns NaN if the first date is invalid"""
        result = difference_in_milliseconds(
            float('nan'),
            datetime(2017, 1, 1)  # Jan 1 2017
        )
        self.assertTrue(math.isnan(result))

    def test_returns_nan_if_second_date_is_invalid(self) -> None:
        """returns NaN if the second date is invalid"""
        result = difference_in_milliseconds(
            datetime(2017, 1, 1),  # Jan 1 2017
            float('nan')
        )
        self.assertTrue(math.isnan(result))

    def test_returns_nan_if_both_dates_are_invalid(self) -> None:
        """returns NaN if both dates are invalid"""
        result = difference_in_milliseconds(float('nan'), float('nan'))
        self.assertTrue(math.isnan(result))


if __name__ == "__main__":
    unittest.main()