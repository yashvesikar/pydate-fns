import unittest
from datetime import datetime

from pydate import closest_to


class TestClosestTo(unittest.TestCase):
    def test_closest_to_1(self):
        """
        returns the date from the given array closest to the given date
        :return:
        """
        date = datetime(2014, 6, 2)
        result = closest_to(
            date,
            [datetime(2015, 7, 31), datetime(2012, 6, 2)],
        )
        self.assertEqual(result, datetime(2015, 7, 31))

    def test_closest_to_2(self):
        """
        works if the closest date from the given array is before the given date
        :return:
        """
        date = datetime(year=2014, month=6, day=2, hour=6, minute=30, second=4, microsecond=500)
        result = closest_to(
            date,
            [
                datetime(
                    year=2014,
                    month=6,
                    day=2,
                    hour=6,
                    minute=30,
                    second=5,
                    microsecond=900,
                ),
                datetime(
                    year=2014,
                    month=6,
                    day=2,
                    hour=6,
                    minute=30,
                    second=3,
                    microsecond=900,
                ),
                datetime(year=2014, month=6, day=2, hour=6, minute=30, second=10),
            ],
        )
        self.assertEqual(
            result,
            datetime(
                year=2014,
                month=6,
                day=2,
                hour=6,
                minute=30,
                second=3,
                microsecond=900,
            ),
        )


if __name__ == "__main__":
    unittest.main()
