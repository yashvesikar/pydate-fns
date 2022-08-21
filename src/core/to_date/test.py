import unittest
from datetime import datetime

from core.to_date.to_date import to_date


class TestIsAfter(unittest.TestCase):
    def test_to_date_1(self):
        """
        returns true if the first date is after the second one
        :return:
        """
        self.assertEqual(to_date(537350400.0), datetime(1987, 1, 11))

    def test_to_date_2(self):
        """
        returns true if the first date is after the second one
        :return:
        """
        self.assertRaises(OverflowError, to_date(1000000000000000000000))


if __name__ == "__main__":
    unittest.main()
