import unittest
from datetime import datetime

from pydate import add


class TestAdd(unittest.TestCase):
    def test_add_values(self) -> None:
        """
        adds the values from the given object
        """
        self.assertEqual(
            add(
                datetime(year=2014, month=8, day=1, hour=10, minute=19, second=50),
                {
                    "years": 2,
                    "months": 9,
                    "weeks": 1,
                    "days": 7,
                    "hours": 5,
                    "minutes": 9,
                    "seconds": 30,
                },
            ),
            datetime(year=2017, month=5, day=15, hour=15, minute=29, second=20),
        )

    def test_add_undefined(self) -> None:
        """
        supports a None value in the duration object
        """

        self.assertEqual(
            add(
                datetime(year=2014, month=8, day=1, hour=10, minute=19, second=50),
                {
                    "years": None,
                    "months": 9,
                    "weeks": 1,
                    "days": 7,
                    "hours": 5,
                    "minutes": 9,
                    "seconds": 30,
                },
            ),
            datetime(year=2015, month=5, day=15, hour=15, minute=29, second=20),
        )

    def test_add_missing(self) -> None:
        """
        supports missing values in the duration object
        """

        self.assertEqual(
            add(
                datetime(year=2014, month=8, day=1, hour=10, minute=19, second=50),
                {
                    "months": 9,
                    "weeks": 1,
                    "days": 7,
                    "hours": 5,
                    "minutes": 9,
                    "seconds": 30,
                },
            ),
            datetime(year=2015, month=5, day=15, hour=15, minute=29, second=20),
        )

    def test_add_empty_duration(self) -> None:
        """
        returns same date object when passed empty duration values
        """

        self.assertEqual(
            add(
                datetime(year=2014, month=8, day=1, hour=10, minute=19, second=50),
                {
                    "years": None,
                    "months": None,
                    "weeks": None,
                    "days": None,
                    "hours": None,
                    "minutes": None,
                    "seconds": None,
                },
            ),
            datetime(year=2014, month=8, day=1, hour=10, minute=19, second=50),
        )

    def test_add_undefined_duration(self) -> None:
        """
        returns same date object when passed undefined duration values
        """

        self.assertEqual(
            add(
                datetime(year=2014, month=8, day=1, hour=10, minute=19, second=50),
                {},
            ),
            datetime(year=2014, month=8, day=1, hour=10, minute=19, second=50),
        )

    def test_add_month_edge(self) -> None:
        """
        throws ValueError if the desired month has fewer days and the provided date is in the last day of a month
        """
        with self.assertRaises(ValueError):
            add(datetime(year=2014, month=11, day=31), {"months": 9})


if __name__ == "__main__":
    unittest.main()
