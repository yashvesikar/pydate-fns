import unittest

from .hours_to_milliseconds import hours_to_milliseconds


class TestHoursToMilliseconds(unittest.TestCase):
    def test_converts_hours_to_milliseconds(self) -> None:
        """
        converts hours to milliseconds
        """
        self.assertEqual(hours_to_milliseconds(1), 3600000)
        self.assertEqual(hours_to_milliseconds(2), 7200000)

    def test_uses_floor_rounding(self) -> None:
        """
        uses floor rounding
        """
        self.assertEqual(hours_to_milliseconds(0.123456), 444441)

    def test_handles_border_values(self) -> None:
        """
        handles border values
        """
        self.assertEqual(hours_to_milliseconds(1.5), 5400000)
        self.assertEqual(hours_to_milliseconds(0), 0)

    def test_works_with_negative_numbers(self) -> None:
        """
        works with negative numbers properly
        """
        self.assertEqual(hours_to_milliseconds(1.234567), 4444441)
        self.assertEqual(hours_to_milliseconds(-1.234567), -4444441)


if __name__ == "__main__":
    unittest.main()