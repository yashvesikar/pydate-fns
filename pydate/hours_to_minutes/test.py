import unittest

from .hours_to_minutes import hours_to_minutes


class TestHoursToMinutes(unittest.TestCase):
    def test_converts_hours_to_minutes(self) -> None:
        """
        converts hours to minutes
        """
        self.assertEqual(hours_to_minutes(1), 60)
        self.assertEqual(hours_to_minutes(2), 120)

    def test_uses_floor_rounding(self) -> None:
        """
        uses floor rounding
        """
        self.assertEqual(hours_to_minutes(0.123456), 7)

    def test_handles_border_values(self) -> None:
        """
        handles border values
        """
        self.assertEqual(hours_to_minutes(1.5), 90)
        self.assertEqual(hours_to_minutes(0), 0)

    def test_works_with_negative_numbers(self) -> None:
        """
        properly works with negative numbers
        """
        self.assertEqual(hours_to_minutes(1.123456), 67)
        self.assertEqual(hours_to_minutes(-1.123456), -67)


if __name__ == "__main__":
    unittest.main()