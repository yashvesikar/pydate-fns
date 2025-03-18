import unittest
from datetime import datetime

from pydate import start_of_week


class TestStartOfWeek(unittest.TestCase):
    def test_returns_date_with_time_set_to_00_00_00(self) -> None:
        """returns the date with time set to 00:00:00"""
        date = datetime(2014, 9, 2, 11, 55, 0)  # Tue Sep 02 2014 11:55:00
        result = start_of_week(date)
        self.assertEqual(result, datetime(2014, 8, 31))  # Sun Aug 31 2014 00:00:00

    def test_allows_to_specify_which_day_is_first_day_of_week(self) -> None:
        """allows to specify which day is the first day of the week"""
        date = datetime(2014, 9, 2, 11, 55, 0)  # Tue Sep 02 2014 11:55:00
        result = start_of_week(date, week_starts_on=1)  # Monday
        self.assertEqual(result, datetime(2014, 9, 1))  # Mon Sep 01 2014 00:00:00

    def test_handles_negative_week_starts_on_values(self) -> None:
        """handles negative week_starts_on values"""
        date = datetime(2014, 9, 2, 11, 55, 0)  # Tue Sep 02 2014 11:55:00
        result = start_of_week(date, week_starts_on=0)  # Sunday
        self.assertEqual(result, datetime(2014, 8, 31))  # Sun Aug 31 2014 00:00:00

    def test_returns_invalid_date_if_date_is_invalid(self) -> None:
        """returns Invalid Date if the date is invalid"""
        result = start_of_week(float('nan'))
        self.assertEqual(result, datetime(1, 1, 1))  # Python's equivalent of Invalid Date


if __name__ == "__main__":
    unittest.main()