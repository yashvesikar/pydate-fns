import unittest
from datetime import datetime
from zoneinfo import ZoneInfo

from .to_naive import to_naive


class TestToNaive(unittest.TestCase):
    def test_to_naive(self) -> None:
        self.assertEqual(
            to_naive(datetime(2014, 9, 25, 12, 30, 45, tzinfo=ZoneInfo("America/New_York"))),
            datetime(2014, 9, 25, 16, 30, 45),
            "should return a naive date",
        )

        # account for dst change
        self.assertEqual(
            to_naive(datetime(2014, 2, 25, 12, 30, 45, tzinfo=ZoneInfo("America/New_York"))),
            datetime(2014, 2, 25, 17, 30, 45),
            "should return a naive date",
        )
