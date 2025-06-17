
from datetime import datetime

from .end_of_hour import end_of_hour


def test_end_of_hour_returns_end_of_hour():
    """Returns the end of an hour for the given date"""
    result = end_of_hour(datetime(2014, 9, 2, 11, 55, 0))
    assert result == datetime(2014, 9, 2, 11, 59, 59, 999999)


def test_end_of_hour_accepts_timestamp():
    """Accepts a timestamp"""
    timestamp = datetime(2014, 9, 2, 11, 55, 0).timestamp()
    result = end_of_hour(timestamp)
    assert result == datetime(2014, 9, 2, 11, 59, 59, 999999)


def test_end_of_hour_does_not_mutate_original_date():
    """Does not mutate the original date"""
    original_date = datetime(2014, 9, 2, 11, 55, 0)
    original_time = original_date.time()
    
    end_of_hour(original_date)
    
    # Original date should remain unchanged
    assert original_date.time() == original_time


def test_end_of_hour_with_different_minutes():
    """Returns consistent end of hour regardless of input minutes"""
    # Different minutes in the same hour should all return the same end of hour
    dates = [
        datetime(2014, 9, 2, 11, 0, 0),      # Start of hour
        datetime(2014, 9, 2, 11, 30, 45),    # Middle of hour  
        datetime(2014, 9, 2, 11, 59, 0),     # Near end of hour
    ]
    
    expected = datetime(2014, 9, 2, 11, 59, 59, 999999)
    
    for date in dates:
        result = end_of_hour(date)
        assert result == expected


def test_end_of_hour_preserves_date_and_hour():
    """Preserves the date and hour while setting time to end of hour"""
    test_dates = [
        datetime(2020, 1, 1, 10, 20, 30),
        datetime(2020, 12, 31, 5, 45, 12),
        datetime(2021, 6, 15, 18, 30, 0),
    ]
    
    for date in test_dates:
        result = end_of_hour(date)
        # Date and hour should be preserved
        assert result.date() == date.date()
        assert result.hour == date.hour
        # Time should be end of hour
        assert result.minute == 59
        assert result.second == 59
        assert result.microsecond == 999999


def test_end_of_hour_different_hours():
    """Works correctly with different hours"""
    test_cases = [
        (datetime(2014, 9, 2, 0, 30, 0), datetime(2014, 9, 2, 0, 59, 59, 999999)),  # Midnight hour
        (datetime(2014, 9, 2, 12, 15, 30), datetime(2014, 9, 2, 12, 59, 59, 999999)),  # Noon hour
        (datetime(2014, 9, 2, 23, 45, 0), datetime(2014, 9, 2, 23, 59, 59, 999999)),  # Last hour of day
    ]
    
    for input_date, expected in test_cases:
        result = end_of_hour(input_date)
        assert result == expected
