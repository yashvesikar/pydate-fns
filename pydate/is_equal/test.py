import unittest
from datetime import datetime

from .is_equal import is_equal


class TestIsEqual(unittest.TestCase):
    def test_is_equal(self) -> None:
        print(datetime(1987, 1, 11), datetime(1987, 1, 11))
        self.assertTrue(is_equal(datetime(1987, 1, 11), datetime(1987, 1, 11)), "should return true if the given dates are equal")

    def test_is_not_equal(self) -> None:
        self.assertFalse(is_equal(datetime(1987, 1, 11), datetime(1987, 1, 12)), "should return false if the given dates are not equal")

    def test_is_equal_timestamps(self) -> None:
        # TODO: want to add this test once pydate is able to handle dirty dates
        pass

    def test_is_equal_bad_first_date(self) -> None:
        with self.assertRaises(TypeError):
            is_equal("1987-01-11", datetime(1987, 1, 11))  # type: ignore

    def test_is_equal_bad_second_date(self) -> None:
        with self.assertRaises(TypeError):
            is_equal(datetime(1987, 1, 11), "1987-01-11")  # type: ignore

    def test_is_equal_bad_both_dates(self) -> None:
        with self.assertRaises(TypeError):
            is_equal("1987-01-11", "1987-01-11")  # type: ignore
