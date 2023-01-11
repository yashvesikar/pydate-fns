import unittest
from datetime import datetime
from zoneinfo import ZoneInfo

from .is_same_month import is_same_month


class TestIsSameMonth(unittest.TestCase):
    def test_is_same_month(self) -> None:
        self.assertTrue(is_same_month(datetime(2014, 9, 4), datetime(2014, 9, 24)), "should return true if the given dates are the same")

    def test_is_not_same_month(self) -> None:
        self.assertFalse(is_same_month(datetime(2014, 9, 4), datetime(2014, 10, 4)), "should return false if the given dates are not the same")

    def test_is_same_month_timezone_aware(self) -> None:

        utc = ZoneInfo("UTC")
        est = ZoneInfo("EST")
        ind = ZoneInfo("Asia/Kolkata")
        self.assertTrue(
            is_same_month(datetime(2014, 9, 30, 19, 30, tzinfo=est), datetime(2014, 10, 1, 0, 30, tzinfo=utc)),
            "should return true if the given dates are the same",
        )

        self.assertTrue(
            is_same_month(datetime(2014, 9, 30, 19, 30, tzinfo=est), datetime(2014, 10, 6, 0, 30, tzinfo=ind)),
            "should return true if the given dates are the same",
        )

    def test_is_not_same_month_timezone_aware(self) -> None:
        utc = ZoneInfo("UTC")
        est = ZoneInfo("EST")

        self.assertFalse(
            is_same_month(datetime(2014, 9, 30, 18, 59, 0, tzinfo=est), datetime(2014, 10, 1, tzinfo=utc)),
            "should return true if the given dates are the same",
        )

    def test_is_same_month_bad_date(self) -> None:
        with self.assertRaises(TypeError):
            is_same_month("2014-09-26", datetime(2014, 9, 4, 23, 59))  # type: ignore

    def test_is_same_month_bad_date2(self) -> None:
        with self.assertRaises(TypeError):
            is_same_month(datetime(2014, 9, 4, 23, 59), "2014-09-26")  # type: ignore

    def test_is_same_month_bad_date3(self) -> None:
        with self.assertRaises(TypeError):
            is_same_month("2014-09-26", "2014-09-26")  # type: ignore
