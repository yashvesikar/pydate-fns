import unittest

from .minutes_to_milliseconds import minutes_to_milliseconds


class TestMinutesToMilliseconds(unittest.TestCase):
    def test_converts_minutes_to_milliseconds(self) -> None:
        """
        converts minutes to milliseconds
        """
        self.assertEqual(minutes_to_milliseconds(1), 60000)
        self.assertEqual(minutes_to_milliseconds(2), 120000)

    def test_uses_floor_rounding(self) -> None:
        """
        uses floor rounding
        """
        self.assertEqual(minutes_to_milliseconds(0.123456), 7407)

    def test_handles_border_values(self) -> None:
        """
        handles border values
        """
        self.assertEqual(minutes_to_milliseconds(1.5), 90000)
        self.assertEqual(minutes_to_milliseconds(0), 0)

    def test_works_with_negative_numbers(self) -> None:
        """
        properly works with negative numbers
        """
        self.assertEqual(minutes_to_milliseconds(1.123456), 67407)
        self.assertEqual(minutes_to_milliseconds(-1.123456), -67407)


if __name__ == "__main__":
    unittest.main()