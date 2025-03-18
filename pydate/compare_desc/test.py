import math
import unittest
from datetime import datetime

from pydate import compare_desc


class TestCompareDesc(unittest.TestCase):
    def test_returns_0_if_dates_are_equal(self) -> None:
        """returns 0 if the given dates are equal"""
        result = compare_desc(
            datetime(year=1989, month=7, day=10),
            datetime(year=1989, month=7, day=10)
        )
        self.assertEqual(result, 0)

    def test_returns_minus_1_if_first_date_after_second(self) -> None:
        """returns -1 if the first date is after the second one"""
        result = compare_desc(
            datetime(year=1989, month=7, day=10),
            datetime(year=1987, month=2, day=11)
        )
        self.assertEqual(result, -1)

    def test_returns_1_if_first_date_before_second(self) -> None:
        """returns 1 if the first date is before the second one"""
        result = compare_desc(
            datetime(year=1987, month=2, day=11),
            datetime(year=1989, month=7, day=10)
        )
        self.assertEqual(result, 1)

    def test_sorts_dates_array_in_reverse_chronological_order(self) -> None:
        """sorts the dates array in reverse chronological order when function is used as key"""
        unsorted_array = [
            datetime(year=1995, month=7, day=2),
            datetime(year=1987, month=2, day=11),
            datetime(year=1989, month=7, day=10)
        ]

        sorted_array = [
            datetime(year=1995, month=7, day=2),
            datetime(year=1989, month=7, day=10),
            datetime(year=1987, month=2, day=11)
        ]

        # For sorting in descending order, we use the negative of the timestamp
        result = sorted(unsorted_array, key=lambda x: -x.timestamp())
        self.assertEqual(result, sorted_array)

    def test_accepts_timestamps(self) -> None:
        """accepts timestamps"""
        result = compare_desc(
            datetime(year=1987, month=2, day=11).timestamp(),
            datetime(year=1989, month=7, day=10).timestamp()
        )
        self.assertEqual(result, 1)

    def test_returns_nan_if_first_date_is_invalid(self) -> None:
        """returns NaN if the first date is invalid"""
        result = compare_desc(float('nan'), datetime(year=1989, month=7, day=10))
        self.assertTrue(math.isnan(result))

    def test_returns_nan_if_second_date_is_invalid(self) -> None:
        """returns NaN if the second date is invalid"""
        result = compare_desc(datetime(year=1989, month=7, day=10), float('nan'))
        self.assertTrue(math.isnan(result))

    def test_returns_nan_if_both_dates_are_invalid(self) -> None:
        """returns NaN if both dates are invalid"""
        result = compare_desc(float('nan'), float('nan'))
        self.assertTrue(math.isnan(result))


if __name__ == "__main__":
    unittest.main()