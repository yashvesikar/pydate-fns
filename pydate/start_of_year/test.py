from datetime import datetime
import pytest
from .start_of_year import start_of_year

def test_returns_date_with_time_set_to_first_day_of_year():
    date = datetime(2014, 9, 2, 11, 55, 0)
    result = start_of_year(date)
    assert result == datetime(2014, 1, 1, 0, 0, 0)

def test_accepts_timestamp():
    date = datetime(2014, 9, 2, 11, 55, 0).timestamp()
    result = start_of_year(date)
    assert result == datetime(2014, 1, 1, 0, 0, 0)

def test_does_not_mutate_original_date():
    date = datetime(2014, 9, 2, 11, 55, 0)
    start_of_year(date)
    assert date == datetime(2014, 9, 2, 11, 55, 0)

def test_handles_dates_before_100_ad():
    initial_date = datetime(9, 1, 5, 0, 0, 0)
    expected_result = datetime(9, 1, 1, 0, 0, 0)
    result = start_of_year(initial_date)
    assert result == expected_result

def test_returns_invalid_date_if_date_is_invalid():
    result = start_of_year(float('nan'))
    with pytest.raises(ValueError):
        result.year  # Accessing any attribute should raise ValueError