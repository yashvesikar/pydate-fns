import math
import unittest
from datetime import datetime, timezone

from pydate import difference_in_seconds


class TestDifferenceInSeconds(unittest.TestCase):
    def test_returns_number_of_seconds_between_dates(self) -> None:
        """returns the number of seconds between dates"""
        result = difference_in_seconds(
            datetime(2014, 7, 2, 12, 30, 20, 0),     # Jul 2 2014, 12:30:20.000
            datetime(2014, 7, 2, 12, 30, 7, 999000)  # Jul 2 2014, 12:30:07.999
        )
        self.assertEqual(result, 12)

    def test_returns_negative_for_earlier_later_date(self) -> None:
        """returns negative number if the first date is before the second"""
        result = difference_in_seconds(
            datetime(2014, 7, 2, 12, 30, 7, 999000),  # Jul 2 2014, 12:30:07.999
            datetime(2014, 7, 2, 12, 30, 20, 0)       # Jul 2 2014, 12:30:20.000
        )
        self.assertEqual(result, -12)

    def test_accepts_timestamps(self) -> None:
        """accepts timestamps"""
        early = datetime(2014, 8, 11, 0, 0, tzinfo=timezone.utc)
        late = datetime(2014, 8, 11, 0, 0, 1, 123000, tzinfo=timezone.utc)
        result = difference_in_seconds(late.timestamp(), early.timestamp())
        self.assertEqual(result, 1)

    def test_rounds_down_when_below_500ms(self) -> None:
        """rounds down when the difference is below 500ms"""
        result = difference_in_seconds(
            datetime(2014, 7, 2, 12, 30, 8, 499000),  # Jul 2 2014, 12:30:08.499
            datetime(2014, 7, 2, 12, 30, 7, 0)        # Jul 2 2014, 12:30:07.000
        )
        self.assertEqual(result, 1)  # not 2

    def test_rounds_up_when_above_500ms(self) -> None:
        """rounds up when the difference is above 500ms"""
        result = difference_in_seconds(
            datetime(2014, 7, 2, 12, 30, 8, 501000),  # Jul 2 2014, 12:30:08.501
            datetime(2014, 7, 2, 12, 30, 7, 0)        # Jul 2 2014, 12:30:07.000
        )
        self.assertEqual(result, 2)  # not 1

    def test_returns_0_if_dates_are_equal(self) -> None:
        """returns 0 if the dates are equal"""
        date = datetime(2014, 8, 5, 0, 0)
        result = difference_in_seconds(date, date)
        self.assertEqual(result, 0)

    def test_returns_nan_if_first_date_is_invalid(self) -> None:
        """returns NaN if the first date is invalid"""
        result = difference_in_seconds(
            float('nan'),
            datetime(2017, 1, 1)  # Jan 1 2017
        )
        self.assertTrue(math.isnan(result))

    def test_returns_nan_if_second_date_is_invalid(self) -> None:
        """returns NaN if the second date is invalid"""
        result = difference_in_seconds(
            datetime(2017, 1, 1),  # Jan 1 2017
            float('nan')
        )
        self.assertTrue(math.isnan(result))

    def test_returns_nan_if_both_dates_are_invalid(self) -> None:
        """returns NaN if both dates are invalid"""
        result = difference_in_seconds(float('nan'), float('nan'))
        self.assertTrue(math.isnan(result))


if __name__ == "__main__":
    unittest.main()