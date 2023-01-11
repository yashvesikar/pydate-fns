import unittest
from datetime import datetime

from .is_sunday import is_sunday


class TestIsSunday(unittest.TestCase):
    def test_is_sunday(self) -> None:
        self.assertTrue(is_sunday(datetime(2014, 9, 28)), "should return true if the given date is a Sunday")

    def test_is_not_sunday(self) -> None:
        self.assertFalse(is_sunday(datetime(2014, 9, 25)), "should return false if the given date is not a Sunday")

    def test_is_sunday_bad_date(self) -> None:
        with self.assertRaises(TypeError):
            is_sunday("2014-09-26")  # type: ignore
