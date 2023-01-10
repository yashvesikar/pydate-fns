import unittest
from datetime import datetime

from .is_first_day_of_month import is_first_day_of_month


class TestIsFirstDayOfMonth(unittest.TestCase):
    def test_is_first_day_of_month(self) -> None:
        self.assertTrue(is_first_day_of_month(datetime(2014, 10, 1)), "should return true if the given date is the first day of a month")

    def test_is_not_first_day_of_month(self) -> None:
        self.assertFalse(is_first_day_of_month(datetime(2014, 10, 2)), "should return false if the given date is not the first day of a month")

    def test_is_first_day_of_month_bad_date(self) -> None:
        with self.assertRaises(TypeError):
            is_first_day_of_month("2014-10-01")  # type: ignore
