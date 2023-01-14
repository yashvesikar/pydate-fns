import unittest
from datetime import datetime
from zoneinfo import ZoneInfo

from .is_same_day import is_same_day


class TestIsSameDay(unittest.TestCase):
    def test_is_same_day(self) -> None:
        self.assertTrue(is_same_day(datetime(2014, 9, 4, 6, 0), datetime(2014, 9, 4, 18, 0)), "should return true if the given dates are the same")

    def test_is_not_same_day(self) -> None:
        self.assertFalse(
            is_same_day(datetime(2014, 9, 4, 23, 59), datetime(2014, 9, 5, 0, 0)), "should return false if the given dates are not the same"
        )

    def test_is_same_day_timezone_aware(self) -> None:

        utc = ZoneInfo("UTC")
        est = ZoneInfo("EST")
        ind = ZoneInfo("Asia/Kolkata")
        self.assertTrue(
            is_same_day(datetime(2014, 9, 4, 18, 59, 0, tzinfo=est), datetime(2014, 9, 4, 23, 59, 0, tzinfo=utc)),
            "should return true if the given dates are the same",
        )

        self.assertTrue(
            is_same_day(datetime(2014, 9, 4, 18, 59, 0, tzinfo=est), datetime(2014, 9, 5, 4, 59, 0, tzinfo=ind)),
            "should return true if the given dates are the same",
        )

    def test_is_not_same_day_timezone_aware(self) -> None:
        utc = ZoneInfo("UTC")
        est = ZoneInfo("EST")

        self.assertFalse(
            is_same_day(datetime(2014, 9, 4, 18, 59, 0, tzinfo=est), datetime(2014, 9, 5, 1, 0, 0, tzinfo=utc)),
            "should return true if the given dates are the same",
        )

    def test_is_same_day_bad_date(self) -> None:
        with self.assertRaises(TypeError):
            is_same_day("2014-09-26", datetime(2014, 9, 4, 23, 59))  # type: ignore

    def test_is_same_day_bad_date2(self) -> None:
        with self.assertRaises(TypeError):
            is_same_day(datetime(2014, 9, 4, 23, 59), "2014-09-26")  # type: ignore

    def test_is_same_day_bad_date3(self) -> None:
        with self.assertRaises(TypeError):
            is_same_day("2014-09-26", "2014-09-26")  # type: ignore
