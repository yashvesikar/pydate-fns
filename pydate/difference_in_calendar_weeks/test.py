import math
import unittest
from datetime import datetime

from pydate import difference_in_calendar_weeks


class TestDifferenceInCalendarWeeks(unittest.TestCase):
    def test_returns_number_of_calendar_weeks_between_dates(self) -> None:
        """returns the number of calendar weeks between the given dates"""
        result = difference_in_calendar_weeks(
            datetime(2014, 7, 8, 18, 0),  # Jul 8 2014, 18:00
            datetime(2014, 6, 29, 6, 0),  # Jun 29 2014, 06:00
        )
        self.assertEqual(result, 1)

    def test_allows_to_specify_which_day_is_first_day_of_week(self) -> None:
        """allows to specify which day is the first day of the week"""
        result = difference_in_calendar_weeks(
            datetime(2014, 7, 8, 18, 0),  # Jul 8 2014, 18:00
            datetime(2014, 6, 29, 6, 0),  # Jun 29 2014, 06:00
            week_starts_on=1  # Monday
        )
        self.assertEqual(result, 2)

    def test_returns_positive_if_second_date_smaller(self) -> None:
        """returns a positive number if the time value of the second date is smaller"""
        result = difference_in_calendar_weeks(
            datetime(2014, 7, 8, 18, 0),  # Jul 8 2014, 18:00
            datetime(2014, 6, 29, 6, 0),  # Jun 29 2014, 06:00
            week_starts_on=1  # Monday
        )
        self.assertEqual(result, 2)

    def test_returns_negative_if_first_date_smaller(self) -> None:
        """returns a negative number if the time value of the first date is smaller"""
        result = difference_in_calendar_weeks(
            datetime(2014, 6, 29, 6, 0),  # Jun 29 2014, 06:00
            datetime(2014, 7, 8, 18, 0),  # Jul 8 2014, 18:00
        )
        self.assertEqual(result, -1)

    def test_accepts_timestamps(self) -> None:
        """accepts timestamps"""
        result = difference_in_calendar_weeks(
            datetime(2014, 7, 12).timestamp(),  # Jul 12 2014
            datetime(2014, 7, 2).timestamp(),   # Jul 2 2014
        )
        self.assertEqual(result, 1)

    def test_less_than_week_different_calendar_weeks(self) -> None:
        """handles dates less than a week apart but in different calendar weeks"""
        result = difference_in_calendar_weeks(
            datetime(2014, 7, 6),  # Jul 6 2014
            datetime(2014, 7, 5),  # Jul 5 2014
        )
        self.assertEqual(result, 1)

    def test_less_than_week_different_calendar_weeks_swapped(self) -> None:
        """same test with swapped dates"""
        result = difference_in_calendar_weeks(
            datetime(2014, 7, 5),  # Jul 5 2014
            datetime(2014, 7, 6),  # Jul 6 2014
        )
        self.assertEqual(result, -1)

    def test_same_days_of_weeks(self) -> None:
        """handles dates with same days of weeks"""
        result = difference_in_calendar_weeks(
            datetime(2014, 7, 9),  # Jul 9 2014
            datetime(2014, 7, 2),  # Jul 2 2014
        )
        self.assertEqual(result, 1)

    def test_returns_0_if_dates_are_same(self) -> None:
        """returns 0 if dates are the same"""
        result = difference_in_calendar_weeks(
            datetime(2014, 9, 5, 0, 0),  # Sep 5 2014, 00:00
            datetime(2014, 9, 5, 0, 0),  # Sep 5 2014, 00:00
        )
        self.assertEqual(result, 0)

    def test_does_not_return_negative_zero(self) -> None:
        """does not return -0 when the given dates are the same"""
        result = difference_in_calendar_weeks(
            datetime(2014, 9, 5, 0, 0),  # Sep 5 2014, 00:00
            datetime(2014, 9, 5, 0, 0),  # Sep 5 2014, 00:00
        )
        self.assertFalse(math.copysign(1, result) < 0)  # Check for negative zero

    def test_returns_nan_if_first_date_is_invalid(self) -> None:
        """returns NaN if the first date is invalid"""
        result = difference_in_calendar_weeks(
            float('nan'),
            datetime(2017, 1, 1),  # Jan 1 2017
        )
        self.assertTrue(math.isnan(result))

    def test_returns_nan_if_second_date_is_invalid(self) -> None:
        """returns NaN if the second date is invalid"""
        result = difference_in_calendar_weeks(
            datetime(2017, 1, 1),  # Jan 1 2017
            float('nan'),
        )
        self.assertTrue(math.isnan(result))

    def test_returns_nan_if_both_dates_are_invalid(self) -> None:
        """returns NaN if both dates are invalid"""
        result = difference_in_calendar_weeks(float('nan'), float('nan'))
        self.assertTrue(math.isnan(result))


if __name__ == "__main__":
    unittest.main()