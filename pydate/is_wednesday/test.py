import unittest
from datetime import datetime

from .is_wednesday import is_wednesday


class TestIsWenesday(unittest.TestCase):
    def test_is_wednesday(self) -> None:
        self.assertTrue(is_wednesday(datetime(2014, 9, 24)), "should return true if the given date is a Wednesday")

    def test_is_not_wednesday(self) -> None:
        self.assertFalse(is_wednesday(datetime(2014, 9, 25)), "should return false if the given date is not a Wednesday")

    def test_is_wednesday_bad_date(self) -> None:
        with self.assertRaises(TypeError):
            is_wednesday("2014-09-26")  # type: ignore
