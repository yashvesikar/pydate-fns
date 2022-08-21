import unittest
from datetime import datetime
from add import add


class TestAdd(unittest.TestCase):
    def test_add_1(self):
        """
        adds the values from the given object
        :return:
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

    def test_add_2(self):
        """
        supports a None value in the duration object
        :return:
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

    def test_add_3(self):
        """
        supports missing values in the duration object
        :return:
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

    def test_add_4(self):
        """
        returns same date object when passed empty duration values
        :return:
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

    def test_add_5(self):
        """
        returns same date object when passed undefined duration values
        :return:
        """

        self.assertEqual(
            add(
                datetime(year=2014, month=8, day=1, hour=10, minute=19, second=50),
                {},
            ),
            datetime(year=2014, month=8, day=1, hour=10, minute=19, second=50),
        )


if __name__ == "__main__":
    unittest.main()
