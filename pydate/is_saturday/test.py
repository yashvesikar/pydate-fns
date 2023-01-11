import unittest
from datetime import datetime

from .is_saturday import is_saturday


class TestIsSaturday(unittest.TestCase):
    def test_is_saturday(self) -> None:
        self.assertTrue(is_saturday(datetime(2014, 9, 27)), "should return true if the given date is a Saturday")

    def test_is_not_saturday(self) -> None:
        self.assertFalse(is_saturday(datetime(2014, 9, 25)), "should return false if the given date is not a Saturday")

    def test_is_saturday_bad_date(self) -> None:
        with self.assertRaises(TypeError):
            is_saturday("2014-09-26")  # type: ignore
