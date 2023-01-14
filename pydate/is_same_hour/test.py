import unittest
from datetime import datetime
from zoneinfo import ZoneInfo

from .is_same_hour import is_same_hour


class TestIsSameHour(unittest.TestCase):
    def test_is_same_hour(self) -> None:
        self.assertTrue(
            is_same_hour(datetime(2014, 9, 4, 6, 0), datetime(2014, 9, 4, 6, 30)), "should return true if the given dates are in the same hour"
        )

    def test_is_not_same_hour(self) -> None:
        self.assertFalse(
            is_same_hour(datetime(2014, 9, 4, 6, 0), datetime(2014, 9, 25, 5, 0)), "should return false if the given dates are not in the same hour"
        )

    def test_is_same_hour_timezone_aware(self) -> None:

        utc = ZoneInfo("UTC")
        est = ZoneInfo("EST")
        self.assertTrue(
            is_same_hour(datetime(2014, 9, 4, 18, 0, 0, tzinfo=est), datetime(2014, 9, 4, 23, 30, 0, tzinfo=utc)),
            "should return true if the given dates are the same",
        )

    def test_is_not_same_hour_timezone_aware(self) -> None:
        utc = ZoneInfo("UTC")
        est = ZoneInfo("EST")

        self.assertFalse(
            is_same_hour(datetime(2014, 9, 4, 17, 59, 0, tzinfo=est), datetime(2014, 9, 4, 23, 59, 0, tzinfo=utc)),
            "should return true if the given dates are the same",
        )

    def test_is_same_hour_bad_date(self) -> None:
        with self.assertRaises(TypeError):
            is_same_hour("2014-09-26", datetime(2014, 9, 26))  # type: ignore

    def test_is_same_hour_bad_date2(self) -> None:
        with self.assertRaises(TypeError):
            is_same_hour(datetime(2014, 9, 26), "2014-09-26")  # type: ignore

    def test_is_same_hour_bad_date3(self) -> None:
        with self.assertRaises(TypeError):
            is_same_hour("2014-09-26", "2014-09-26")  # type: ignore
