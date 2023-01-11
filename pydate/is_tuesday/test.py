import unittest
from datetime import datetime

from .is_tuesday import is_tuesday


class TestIsTuesday(unittest.TestCase):
    def test_is_tuesday(self) -> None:
        self.assertTrue(is_tuesday(datetime(2014, 9, 23)), "should return true if the given date is a Tuesday")

    def test_is_not_tueday(self) -> None:
        self.assertFalse(is_tuesday(datetime(2014, 9, 25)), "should return false if the given date is not a Tuesday")

    def test_is_tuesday_bad_date(self) -> None:
        with self.assertRaises(TypeError):
            is_tuesday("2014-09-26")  # type: ignore
