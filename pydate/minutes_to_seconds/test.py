import unittest

from .minutes_to_seconds import minutes_to_seconds


class TestMinutesToSeconds(unittest.TestCase):
    def test_converts_minutes_to_seconds(self) -> None:
        """
        converts minutes to seconds
        """
        self.assertEqual(minutes_to_seconds(1), 60)
        self.assertEqual(minutes_to_seconds(2), 120)

    def test_uses_floor_rounding(self) -> None:
        """
        uses floor rounding
        """
        self.assertEqual(minutes_to_seconds(0.123456), 7)

    def test_handles_border_values(self) -> None:
        """
        handles border values
        """
        self.assertEqual(minutes_to_seconds(1.5), 90)
        self.assertEqual(minutes_to_seconds(0), 0)

    def test_works_with_negative_numbers(self) -> None:
        """
        properly works with negative numbers
        """
        self.assertEqual(minutes_to_seconds(1.123456), 67)
        self.assertEqual(minutes_to_seconds(-1.123456), -67)


if __name__ == "__main__":
    unittest.main()