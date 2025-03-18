import unittest

from .seconds_to_milliseconds import seconds_to_milliseconds


class TestSecondsToMilliseconds(unittest.TestCase):
    def test_converts_seconds_to_milliseconds(self) -> None:
        """
        converts seconds to milliseconds
        """
        self.assertEqual(seconds_to_milliseconds(1), 1000)
        self.assertEqual(seconds_to_milliseconds(2), 2000)

    def test_uses_floor_rounding(self) -> None:
        """
        uses floor rounding
        """
        self.assertEqual(seconds_to_milliseconds(0.123456), 123)

    def test_handles_border_values(self) -> None:
        """
        handles border values
        """
        self.assertEqual(seconds_to_milliseconds(1.5), 1500)
        self.assertEqual(seconds_to_milliseconds(0), 0)

    def test_works_with_negative_numbers(self) -> None:
        """
        properly works with negative numbers
        """
        self.assertEqual(seconds_to_milliseconds(1.123456), 1123)
        self.assertEqual(seconds_to_milliseconds(-1.123456), -1123)


if __name__ == "__main__":
    unittest.main()