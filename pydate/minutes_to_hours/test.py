import unittest

from .minutes_to_hours import minutes_to_hours


class TestMinutesToHours(unittest.TestCase):
    def test_converts_minutes_to_hours(self) -> None:
        """
        converts minutes to hours
        """
        self.assertEqual(minutes_to_hours(60), 1)
        self.assertEqual(minutes_to_hours(120), 2)

    def test_uses_floor_rounding(self) -> None:
        """
        uses floor rounding
        """
        self.assertEqual(minutes_to_hours(61), 1)
        self.assertEqual(minutes_to_hours(59), 0)

    def test_handles_border_values(self) -> None:
        """
        handles border values
        """
        self.assertEqual(minutes_to_hours(90), 1)
        self.assertEqual(minutes_to_hours(0), 0)

    def test_works_with_negative_numbers(self) -> None:
        """
        properly works with negative numbers
        """
        self.assertEqual(minutes_to_hours(67), 1)
        self.assertEqual(minutes_to_hours(-67), -1)


if __name__ == "__main__":
    unittest.main()