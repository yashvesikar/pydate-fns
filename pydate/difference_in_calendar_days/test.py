import math
import unittest
from datetime import datetime, timedelta, timezone

from pydate import difference_in_calendar_days


class TestDifferenceInCalendarDays(unittest.TestCase):
    def test_returns_number_of_calendar_days_between_dates(self) -> None:
        """returns the number of calendar days between the given dates"""
        result = difference_in_calendar_days(
            datetime(2012, 7, 2, 18, 0),  # Jul 2 2012, 18:00
            datetime(2011, 7, 2, 6, 0),   # Jul 2 2011, 06:00
        )
        self.assertEqual(result, 366)  # Leap year

    def test_returns_negative_if_first_date_smaller(self) -> None:
        """returns a negative number if the time value of the first date is smaller"""
        result = difference_in_calendar_days(
            datetime(2011, 7, 2, 6, 0),   # Jul 2 2011, 06:00
            datetime(2012, 7, 2, 18, 0),  # Jul 2 2012, 18:00
        )
        self.assertEqual(result, -366)

    def test_accepts_timestamps(self) -> None:
        """accepts timestamps"""
        result = difference_in_calendar_days(
            datetime(2014, 9, 5, 18, 0).timestamp(),  # Sep 5 2014, 18:00
            datetime(2014, 9, 4, 6, 0).timestamp(),   # Sep 4 2014, 06:00
        )
        self.assertEqual(result, 1)

    def test_different_calendar_days_less_than_day(self) -> None:
        """handles dates in different calendar days but less than 24 hours apart"""
        result = difference_in_calendar_days(
            datetime(2014, 9, 5, 0, 0),   # Sep 5 2014, 00:00
            datetime(2014, 9, 4, 23, 59),  # Sep 4 2014, 23:59
        )
        self.assertEqual(result, 1)

    def test_different_calendar_days_less_than_day_swapped(self) -> None:
        """same test with swapped dates"""
        result = difference_in_calendar_days(
            datetime(2014, 9, 4, 23, 59),  # Sep 4 2014, 23:59
            datetime(2014, 9, 5, 0, 0),    # Sep 5 2014, 00:00
        )
        self.assertEqual(result, -1)

    def test_same_time_different_days(self) -> None:
        """handles dates with same time on different days"""
        result = difference_in_calendar_days(
            datetime(2014, 9, 6, 0, 0),  # Sep 6 2014, 00:00
            datetime(2014, 9, 5, 0, 0),  # Sep 5 2014, 00:00
        )
        self.assertEqual(result, 1)

    def test_same_dates(self) -> None:
        """returns 0 for same dates"""
        result = difference_in_calendar_days(
            datetime(2014, 9, 5, 0, 0),  # Sep 5 2014, 00:00
            datetime(2014, 9, 5, 0, 0),  # Sep 5 2014, 00:00
        )
        self.assertEqual(result, 0)

    def test_does_not_return_negative_zero(self) -> None:
        """does not return -0 when the given dates are the same"""
        result = difference_in_calendar_days(
            datetime(2014, 9, 5, 0, 0),  # Sep 5 2014, 00:00
            datetime(2014, 9, 5, 0, 0),  # Sep 5 2014, 00:00
        )
        self.assertFalse(math.copysign(1, result) < 0)  # Check for negative zero

    def test_returns_nan_for_invalid_first_date(self) -> None:
        """returns NaN if the first date is invalid"""
        result = difference_in_calendar_days(
            float('nan'),
            datetime(2017, 1, 1),  # Jan 1 2017
        )
        self.assertTrue(math.isnan(result))

    def test_returns_nan_for_invalid_second_date(self) -> None:
        """returns NaN if the second date is invalid"""
        result = difference_in_calendar_days(
            datetime(2017, 1, 1),  # Jan 1 2017
            float('nan'),
        )
        self.assertTrue(math.isnan(result))

    def test_returns_nan_for_invalid_both_dates(self) -> None:
        """returns NaN if both dates are invalid"""
        result = difference_in_calendar_days(float('nan'), float('nan'))
        self.assertTrue(math.isnan(result))

    def test_handles_dst_start(self) -> None:
        """handles dates across DST start correctly"""
        # Create dates around a typical DST start (spring forward)
        base = datetime(2024, 3, 10, 1, 0, tzinfo=timezone.utc)  # A typical DST start date
        day_before = base - timedelta(days=1)
        day_after = base + timedelta(days=1)

        # Test across DST boundary
        result = difference_in_calendar_days(day_after, day_before)
        self.assertEqual(result, 2)  # Should be 2 calendar days apart

    def test_handles_dst_end(self) -> None:
        """handles dates across DST end correctly"""
        # Create dates around a typical DST end (fall back)
        base = datetime(2024, 11, 3, 1, 0, tzinfo=timezone.utc)  # A typical DST end date
        day_before = base - timedelta(days=1)
        day_after = base + timedelta(days=1)

        # Test across DST boundary
        result = difference_in_calendar_days(day_after, day_before)
        self.assertEqual(result, 2)  # Should be 2 calendar days apart


if __name__ == "__main__":
    unittest.main()