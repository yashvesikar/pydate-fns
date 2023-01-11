import unittest
from datetime import datetime

from .is_thursday import is_thursday


class TestIsThursday(unittest.TestCase):
    def test_is_thursday(self) -> None:
        self.assertTrue(is_thursday(datetime(2014, 9, 25)), "should return true if the given date is a Thursday")

    def test_is_not_thursday(self) -> None:
        self.assertFalse(is_thursday(datetime(2014, 9, 24)), "should return false if the given date is not a Thursday")

    def test_is_thursday_bad_date(self) -> None:
        with self.assertRaises(TypeError):
            is_thursday("2014-09-26")  # type: ignore
