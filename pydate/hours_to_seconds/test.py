import unittest

from .hours_to_seconds import hours_to_seconds


class TestHoursToSeconds(unittest.TestCase):
    def test_converts_hours_to_seconds(self) -> None:
        """
        converts hours to seconds
        """
        self.assertEqual(hours_to_seconds(1), 3600)
        self.assertEqual(hours_to_seconds(2), 7200)

    def test_uses_floor_rounding(self) -> None:
        """
        uses floor rounding
        """
        self.assertEqual(hours_to_seconds(0.123456), 444)

    def test_handles_border_values(self) -> None:
        """
        handles border values
        """
        self.assertEqual(hours_to_seconds(1.5), 5400)
        self.assertEqual(hours_to_seconds(0), 0)

    def test_works_with_negative_numbers(self) -> None:
        """
        properly works with negative numbers
        """
        self.assertEqual(hours_to_seconds(1.123456), 4044)
        self.assertEqual(hours_to_seconds(-1.123456), -4044)


if __name__ == "__main__":
    unittest.main()