import unittest

from .seconds_to_minutes import seconds_to_minutes


class TestSecondsToMinutes(unittest.TestCase):
    def test_converts_seconds_to_minutes(self) -> None:
        """
        converts seconds to minutes
        """
        self.assertEqual(seconds_to_minutes(60), 1)
        self.assertEqual(seconds_to_minutes(120), 2)

    def test_uses_floor_rounding(self) -> None:
        """
        uses floor rounding
        """
        self.assertEqual(seconds_to_minutes(61), 1)
        self.assertEqual(seconds_to_minutes(59), 0)

    def test_handles_border_values(self) -> None:
        """
        handles border values
        """
        self.assertEqual(seconds_to_minutes(90), 1)
        self.assertEqual(seconds_to_minutes(0), 0)

    def test_works_with_negative_numbers(self) -> None:
        """
        properly works with negative numbers
        """
        self.assertEqual(seconds_to_minutes(67), 1)
        self.assertEqual(seconds_to_minutes(-67), -1)


if __name__ == "__main__":
    unittest.main()