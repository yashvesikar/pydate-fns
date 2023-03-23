
import unittest
from zoneinfo import ZoneInfo

from freezegun import freeze_time
from datetime import datetime
from .is_future import is_future

class TestIsFuture(unittest.TestCase):

    @freeze_time("2014-09-25")
    def test_is_future(self) -> None:
        self.assertTrue(is_future(datetime(2014, 9, 30)), "should return true if the given date is in the future")

    @freeze_time("2014-09-25")
    def test_is_not_future(self) -> None:
        self.assertFalse(is_future(datetime(2014, 9, 1)), "should return false if the given date is not in the future")

    @freeze_time("2014-09-25")
    def test_is_future_timezone_aware(self) -> None:
        est = ZoneInfo("EST")
        self.assertTrue(
            is_future(datetime(2014, 9, 30, tzinfo=est)),
            "should return true if the given date is in the future",
        )

    @freeze_time("2014-09-25")
    def test_is_not_future_timezone_aware(self) -> None:
        est = ZoneInfo("EST")
        self.assertFalse(
            is_future(datetime(2014, 9, 1, tzinfo=est)),
            "should return false if the given date is not in the future",
        )

    @freeze_time("2014-09-25")
    def test_is_now(self):
        self.assertFalse(is_future(datetime(2014, 9, 25)), "should return false if the given date is now")

    def test_is_future_bad_date(self) -> None:
        with self.assertRaises(TypeError):
            is_future("2014-09-26")


