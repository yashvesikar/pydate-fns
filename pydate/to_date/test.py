import unittest
from datetime import datetime

from pydate import to_date


class TestToDate(unittest.TestCase):
    def test_to_date_1(self):
        """
        :return:
        """
        self.assertEqual(to_date(537350400.0), datetime(1987, 1, 11, 8, 0))

    def test_to_date_2(self):
        """
        :return:
        """
        with self.assertRaises(OverflowError):
            to_date(1000000000000000000000)


if __name__ == "__main__":
    unittest.main()
