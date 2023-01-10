import unittest
from datetime import datetime

from .is_friday import is_friday


class TestIsFriday(unittest.TestCase):
    def test_is_friday(self) -> None:
        self.assertTrue(is_friday(datetime(2014, 9, 26)), "should return true if the given date is a Friday")

    def test_is_not_friday(self) -> None:
        self.assertFalse(is_friday(datetime(2014, 9, 25)), "should return false if the given date is not a Friday")

    def test_is_friday_bad_date(self) -> None:
        with self.assertRaises(TypeError):
            is_friday("2014-09-26")  # type: ignore
