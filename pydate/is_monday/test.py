import unittest
from datetime import datetime

from .is_monday import is_monday


class TestIsFriday(unittest.TestCase):
    def test_is_monday(self) -> None:
        self.assertTrue(is_monday(datetime(2014, 9, 22)), "should return true if the given date is a Friday")

    def test_is_not_tuesday(self) -> None:
        self.assertFalse(is_monday(datetime(2014, 9, 25)), "should return false if the given date is not a Friday")

    def test_is_monday_bad_date(self) -> None:
        with self.assertRaises(TypeError):
            is_monday("2014-09-26")  # type: ignore
