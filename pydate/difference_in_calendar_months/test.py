import math
import unittest
from datetime import datetime

from pydate import difference_in_calendar_months


class TestDifferenceInCalendarMonths(unittest.TestCase):
    def test_returns_number_of_calendar_months_between_dates(self) -> None:
        """returns the number of calendar months between the given dates"""
        result = difference_in_calendar_months(
            datetime(2012, 7, 2, 18, 0),  # Jul 2 2012, 18:00
            datetime(2011, 7, 2, 6, 0),   # Jul 2 2011, 06:00
        )
        self.assertEqual(result, 12)

    def test_returns_negative_if_first_date_smaller(self) -> None:
        """returns a negative number if the time value of the first date is smaller"""
        result = difference_in_calendar_months(
            datetime(2011, 7, 2, 6, 0),   # Jul 2 2011, 06:00
            datetime(2012, 7, 2, 18, 0),  # Jul 2 2012, 18:00
        )
        self.assertEqual(result, -12)

    def test_accepts_timestamps(self) -> None:
        """accepts timestamps"""
        result = difference_in_calendar_months(
            datetime(2014, 8, 2).timestamp(),  # Aug 2 2014
            datetime(2010, 7, 2).timestamp(),  # Jul 2 2010
        )
        self.assertEqual(result, 49)

    def test_different_months_less_than_month_apart(self) -> None:
        """returns 1 when dates are in different months but less than a month apart"""
        result = difference_in_calendar_months(
            datetime(2014, 9, 1),   # Sep 1 2014
            datetime(2014, 8, 31),  # Aug 31 2014
        )
        self.assertEqual(result, 1)

    def test_swapped_dates_with_month_difference(self) -> None:
        """returns -1 for swapped dates with a month difference"""
        result = difference_in_calendar_months(
            datetime(2014, 8, 31),  # Aug 31 2014
            datetime(2014, 9, 1),   # Sep 1 2014
        )
        self.assertEqual(result, -1)

    def test_handles_same_day_of_month(self) -> None:
        """handles same day of month correctly"""
        result = difference_in_calendar_months(
            datetime(2014, 9, 6),  # Sep 6 2014
            datetime(2014, 8, 6),  # Aug 6 2014
        )
        self.assertEqual(result, 1)

    def test_returns_0_for_same_dates(self) -> None:
        """returns 0 when given the same dates"""
        result = difference_in_calendar_months(
            datetime(2014, 9, 5, 0, 0),  # Sep 5 2014, 00:00
            datetime(2014, 9, 5, 0, 0),  # Sep 5 2014, 00:00
        )
        self.assertEqual(result, 0)

    def test_does_not_return_negative_zero(self) -> None:
        """does not return -0 for the same dates"""
        result = difference_in_calendar_months(
            datetime(2014, 9, 5, 0, 0),  # Sep 5 2014, 00:00
            datetime(2014, 9, 5, 0, 0),  # Sep 5 2014, 00:00
        )
        self.assertFalse(math.copysign(1, result) < 0)  # Check for negative zero

    def test_returns_nan_for_invalid_first_date(self) -> None:
        """returns NaN if the first date is invalid"""
        result = difference_in_calendar_months(
            float('nan'),
            datetime(2017, 1, 1),  # Jan 1 2017
        )
        self.assertTrue(math.isnan(result))

    def test_returns_nan_for_invalid_second_date(self) -> None:
        """returns NaN if the second date is invalid"""
        result = difference_in_calendar_months(
            datetime(2017, 1, 1),  # Jan 1 2017
            float('nan'),
        )
        self.assertTrue(math.isnan(result))

    def test_returns_nan_for_invalid_both_dates(self) -> None:
        """returns NaN if both dates are invalid"""
        result = difference_in_calendar_months(float('nan'), float('nan'))
        self.assertTrue(math.isnan(result))


if __name__ == "__main__":
    unittest.main()