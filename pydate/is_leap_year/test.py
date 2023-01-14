import unittest
from datetime import datetime

from .is_leap_year import is_leap_year


class TestIsLeapYear(unittest.TestCase):
    def test_is_leap_year(self) -> None:
        self.assertTrue(is_leap_year(datetime(2012, 7, 2)), "returns True if the date is in a leap year")

    def test_is_not_leap_year(self) -> None:
        self.assertFalse(is_leap_year(datetime(2014, 7, 2)), "returns False if the date is not in a leap year")

    def test_is_not_leap_year_century(self) -> None:
        self.assertFalse(is_leap_year(datetime(2100, 7, 2)), "works for years divisible by 100 but not 400")

    def test_is_leap_year_century(self) -> None:
        self.assertTrue(is_leap_year(datetime(2000, 7, 2)), "works for years divisible by 400")

    def test_is_leap_year_bad_input(self) -> None:
        with self.assertRaises(TypeError):
            is_leap_year("2014-10-31")  # type: ignore
