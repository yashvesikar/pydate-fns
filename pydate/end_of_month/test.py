from datetime import datetime
import pytest
from .end_of_month import end_of_month

def test_returns_date_with_time_set_to_last_millisecond_and_last_day_of_month():
    date = datetime(2014, 9, 2, 11, 55, 0)
    result = end_of_month(date)
    assert result == datetime(2014, 9, 30, 23, 59, 59, 999999)

def test_accepts_timestamp():
    date = datetime(2014, 9, 2, 11, 55, 0).timestamp()
    result = end_of_month(date)
    assert result == datetime(2014, 9, 30, 23, 59, 59, 999999)

def test_does_not_mutate_original_date():
    date = datetime(2014, 9, 2, 11, 55, 0)
    end_of_month(date)
    assert date == datetime(2014, 9, 2, 11, 55, 0)

def test_works_for_last_month_in_year():
    date = datetime(2014, 12, 1, 0, 0, 0)
    result = end_of_month(date)
    assert result == datetime(2014, 12, 31, 23, 59, 59, 999999)

def test_works_for_last_day_of_month():
    date = datetime(2014, 10, 31)
    result = end_of_month(date)
    assert result == datetime(2014, 10, 31, 23, 59, 59, 999999)

def test_returns_invalid_date_if_date_is_invalid():
    result = end_of_month(float('nan'))
    with pytest.raises(ValueError):
        result.year  # Accessing any attribute should raise ValueError