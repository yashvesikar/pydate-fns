import unittest
from datetime import datetime

from .is_date import is_date


class TestIsDate(unittest.TestCase):
    def test_is_date(self) -> None:

        self.assertTrue(is_date(datetime.now()), "should return true if the given value is an instance of datetime")

    def test_is_not_date(self) -> None:
        self.assertFalse(is_date("2021-01-01"), "should return false if the given value is not an instance of datetime")
