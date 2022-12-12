import unittest
from datetime import datetime

from pydate import sub_months


class TestSubMonths(unittest.TestCase):
    def test_subtracts_the_given_number_of_months(self):
        result = sub_months(datetime(2015, 2, 1), 5)
        self.assertEqual(result, datetime(2014, 9, 1))

    def test_accepts_a_timestamp(self):
        result = sub_months(datetime(2015, 9, 1), 12)
        self.assertEqual(result, datetime(2014, 9, 1))

    def test_does_not_mutate_the_original_date(self):
        date = datetime(2014, 9, 1)
        sub_months(date, 12)
        self.assertEqual(date, datetime(2014, 9, 1))

    def test_works_well_if_the_desired_month_has_fewer_days_and_the_provided_date_is_in_the_last_day_of_a_month(self):
        date = datetime(2014, 12, 31)
        result = sub_months(date, 3)
        self.assertEqual(result, datetime(2014, 9, 30))

    def test_handles_dates_before_100_AD(self):
        initial_date = datetime(1, 3, 31)
        expected_result = datetime(1, 2, 28)
        result = sub_months(initial_date, 1)

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
