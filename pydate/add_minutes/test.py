import unittest
from datetime import datetime

from pydate import add_minutes


class TestAddMinutes(unittest.TestCase):
    def test_adds_given_number_of_minutes(self) -> None:
        """adds the given number of minutes"""
        result = add_minutes(
            datetime(2014, 7, 10, 12, 0),  # Jul 10 2014, 12:00
            30
        )
        self.assertEqual(result, datetime(2014, 7, 10, 12, 30))  # Jul 10 2014, 12:30

    def test_accepts_timestamp(self) -> None:
        """accepts a timestamp"""
        result = add_minutes(
            datetime(2014, 7, 10, 12, 0).timestamp(),  # Jul 10 2014, 12:00
            20
        )
        self.assertEqual(result, datetime(2014, 7, 10, 12, 20))  # Jul 10 2014, 12:20

    def test_does_not_mutate_original_date(self) -> None:
        """does not mutate the original date"""
        date = datetime(2014, 7, 10, 12, 0)  # Jul 10 2014, 12:00
        add_minutes(date, 25)
        self.assertEqual(date, datetime(2014, 7, 10, 12, 0))  # Original date unchanged

    def test_returns_invalid_date_if_date_invalid(self) -> None:
        """returns Invalid Date if the given date is invalid"""
        result = add_minutes(float('nan'), 30)
        self.assertEqual(result, datetime(1, 1, 1, 0, 0, 0, 0))  # Python's equivalent of Invalid Date

    def test_returns_invalid_date_if_amount_nan(self) -> None:
        """returns Invalid Date if the given amount is NaN"""
        result = add_minutes(datetime(2014, 7, 10, 12, 0), float('nan'))
        self.assertEqual(result, datetime(1, 1, 1, 0, 0, 0, 0))  # Python's equivalent of Invalid Date

    def test_handles_dst_transitions(self) -> None:
        """handles dates across DST transitions"""
        # Note: This test might need adjustment based on your timezone
        # Testing adding minutes across a typical DST transition
        spring_transition = datetime(2024, 3, 10, 1, 45)  # Just before spring forward
        result = add_minutes(spring_transition, 30)
        self.assertEqual(result, datetime(2024, 3, 10, 2, 15))

        fall_transition = datetime(2024, 11, 3, 1, 45)  # Just before fall back
        result = add_minutes(fall_transition, 30)
        self.assertEqual(result, datetime(2024, 11, 3, 2, 15))


if __name__ == "__main__":
    unittest.main()