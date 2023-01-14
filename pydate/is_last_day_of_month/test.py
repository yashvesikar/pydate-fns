import unittest
from datetime import datetime

from .is_last_day_of_month import is_last_day_of_month


class TestIsLastDayOfMonth(unittest.TestCase):
    def test_is_last_day_of_month(self) -> None:
        self.assertTrue(is_last_day_of_month(datetime(2014, 10, 31)))

    def test_is_not_last_day_of_month(self) -> None:
        self.assertFalse(is_last_day_of_month(datetime(2014, 10, 30)))

    def test_is_last_day_of_month_with_leap_year(self) -> None:
        self.assertTrue(is_last_day_of_month(datetime(2016, 2, 29)))

    def test_is_not_last_day_of_month_with_leap_year(self) -> None:
        self.assertFalse(is_last_day_of_month(datetime(2016, 2, 28)))

    def test_is_last_day_of_month_bad_input(self) -> None:
        with self.assertRaises(TypeError):
            is_last_day_of_month("2014-10-31")  # type: ignore
