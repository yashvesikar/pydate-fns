import unittest
from datetime import datetime
from zoneinfo import ZoneInfo

from .is_same_year import is_same_year


class TestIsSameyear(unittest.TestCase):
    def test_is_same_year(self) -> None:
        self.assertTrue(is_same_year(datetime(2014, 9, 4), datetime(2014, 12, 1)), "should return true if the given dates are the same")

    def test_is_not_same_year(self) -> None:
        self.assertFalse(is_same_year(datetime(2014, 9, 4), datetime(2015, 3, 5)), "should return false if the given dates are not the same")

    def test_is_same_year_timezone_aware(self) -> None:

        utc = ZoneInfo("UTC")
        est = ZoneInfo("EST")
        ind = ZoneInfo("Asia/Kolkata")
        self.assertTrue(
            is_same_year(datetime(2014, 12, 31, 13, 59, tzinfo=est), datetime(2014, 12, 31, 18, 59, tzinfo=utc)),
            "should return true if the given dates are the same",
        )

        self.assertTrue(
            is_same_year(datetime(2014, 12, 31, 11, 59, tzinfo=est), datetime(2014, 12, 31, 11, 59, tzinfo=ind)),
            "should return true if the given dates are the same",
        )

    def test_is_not_same_year_timezone_aware(self) -> None:
        utc = ZoneInfo("UTC")
        est = ZoneInfo("EST")

        self.assertFalse(
            is_same_year(datetime(2014, 12, 31, 18, 59, tzinfo=est), datetime(2015, 1, 1, tzinfo=utc)),
            "should return true if the given dates are the same",
        )

    def test_is_same_year_bad_date(self) -> None:
        with self.assertRaises(TypeError):
            is_same_year("2014-09-26", datetime(2014, 9, 4, 23, 59))  # type: ignore

    def test_is_same_year_bad_date2(self) -> None:
        with self.assertRaises(TypeError):
            is_same_year(datetime(2014, 9, 4, 23, 59), "2014-09-26")  # type: ignore

    def test_is_same_year_bad_date3(self) -> None:
        with self.assertRaises(TypeError):
            is_same_year("2014-09-26", "2014-09-26")  # type: ignore
