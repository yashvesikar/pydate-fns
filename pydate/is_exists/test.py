import unittest
from datetime import datetime

from .is_exists import is_exists


class Testis_exists(unittest.TestCase):
    def test_is_exists(self) -> None:
        self.assertTrue(is_exists(2018, 1, 31), "should return true if the given date is valid")

    def test_is_not_exists(self) -> None:
        self.assertFalse(is_exists(2018, 2, 31), "should return false if the given date is invalid")
