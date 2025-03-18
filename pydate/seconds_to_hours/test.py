import unittest

from .seconds_to_hours import seconds_to_hours


class TestSecondsToHours(unittest.TestCase):
    def test_converts_seconds_to_hours(self) -> None:
        """
        converts seconds to hours
        """
        self.assertEqual(seconds_to_hours(3600), 1)
        self.assertEqual(seconds_to_hours(7200), 2)

    def test_uses_floor_rounding(self) -> None:
        """
        uses floor rounding
        """
        self.assertEqual(seconds_to_hours(3601), 1)
        self.assertEqual(seconds_to_hours(3599), 0)

    def test_handles_border_values(self) -> None:
        """
        handles border values
        """
        self.assertEqual(seconds_to_hours(5400), 1)
        self.assertEqual(seconds_to_hours(0), 0)

    def test_works_with_negative_numbers(self) -> None:
        """
        properly works with negative numbers
        """
        self.assertEqual(seconds_to_hours(4044), 1)
        self.assertEqual(seconds_to_hours(-4044), -1)


if __name__ == "__main__":
    unittest.main()