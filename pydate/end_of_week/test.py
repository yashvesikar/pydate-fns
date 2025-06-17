
from datetime import datetime

from .end_of_week import end_of_week


def test_end_of_week_returns_end_of_week():
    """Returns the end of a week for the given date"""
    # Tuesday Sept 2, 2014 should end on Saturday Sept 6, 2014
    result = end_of_week(datetime(2014, 9, 2, 11, 55, 0))
    assert result == datetime(2014, 9, 6, 23, 59, 59, 999999)


def test_end_of_week_with_monday_start():
    """Returns the end of a week when week starts on Monday"""
    # Tuesday Sept 2, 2014 should end on Sunday Sept 7, 2014 when week starts Monday
    result = end_of_week(datetime(2014, 9, 2, 11, 55, 0), week_starts_on=1)
    assert result == datetime(2014, 9, 7, 23, 59, 59, 999999)


def test_end_of_week_accepts_timestamp():
    """Accepts a timestamp"""
    timestamp = datetime(2014, 9, 2, 11, 55, 0).timestamp()
    result = end_of_week(timestamp)
    assert result == datetime(2014, 9, 6, 23, 59, 59, 999999)


def test_end_of_week_does_not_mutate_original_date():
    """Does not mutate the original date"""
    original_date = datetime(2014, 9, 2, 11, 55, 0)
    original_time = original_date.time()
    
    end_of_week(original_date)
    
    # Original date should remain unchanged
    assert original_date.time() == original_time


def test_end_of_week_different_week_starts():
    """Works correctly with different week start days"""
    # Testing with Wednesday April 10, 2024
    date = datetime(2024, 4, 10, 12, 0, 0)  # Wednesday
    
    # Sunday start (default): Week ends on Saturday
    result_sunday = end_of_week(date, week_starts_on=0)
    assert result_sunday == datetime(2024, 4, 13, 23, 59, 59, 999999)  # Saturday
    
    # Monday start: Week ends on Sunday
    result_monday = end_of_week(date, week_starts_on=1)
    assert result_monday == datetime(2024, 4, 14, 23, 59, 59, 999999)  # Sunday
    
    # Tuesday start: Week ends on Monday  
    result_tuesday = end_of_week(date, week_starts_on=2)
    assert result_tuesday == datetime(2024, 4, 15, 23, 59, 59, 999999)  # Monday
    
    # Wednesday start: Week ends on Tuesday (same day should end on next Tuesday)
    result_wednesday = end_of_week(date, week_starts_on=3)
    assert result_wednesday == datetime(2024, 4, 16, 23, 59, 59, 999999)  # Tuesday


def test_end_of_week_edge_cases():
    """Tests edge cases for end of week calculation"""
    # Test Sunday with Sunday start - should be same day
    sunday = datetime(2024, 4, 7, 10, 0, 0)  # Sunday
    result = end_of_week(sunday, week_starts_on=0)
    assert result == datetime(2024, 4, 13, 23, 59, 59, 999999)  # Following Saturday
    
    # Test Saturday with Sunday start - should be same day
    saturday = datetime(2024, 4, 6, 10, 0, 0)  # Saturday
    result = end_of_week(saturday, week_starts_on=0)
    assert result == datetime(2024, 4, 6, 23, 59, 59, 999999)  # Same Saturday


def test_end_of_week_preserves_date_logic():
    """Preserves correct date logic across different scenarios"""
    test_cases = [
        # (input_date, week_starts_on, expected_end_date)
        (datetime(2014, 9, 1, 10, 0), 0, datetime(2014, 9, 6, 23, 59, 59, 999999)),  # Monday -> Saturday
        (datetime(2014, 9, 2, 10, 0), 0, datetime(2014, 9, 6, 23, 59, 59, 999999)),  # Tuesday -> Saturday
        (datetime(2014, 9, 6, 10, 0), 0, datetime(2014, 9, 6, 23, 59, 59, 999999)),  # Saturday -> Saturday
        (datetime(2014, 9, 7, 10, 0), 0, datetime(2014, 9, 13, 23, 59, 59, 999999)), # Sunday -> next Saturday
    ]
    
    for input_date, week_start, expected in test_cases:
        result = end_of_week(input_date, week_starts_on=week_start)
        assert result == expected, f"Failed for {input_date} with week_starts_on={week_start}"
