from datetime import datetime
import pytest
from .end_of_minute import end_of_minute

def test_returns_date_with_time_set_to_last_millisecond_before_minute_ends():
    date = datetime(2014, 12, 1, 22, 15)
    result = end_of_minute(date)
    assert result == datetime(2014, 12, 1, 22, 15, 59, 999999)

def test_accepts_timestamp():
    date = datetime(2014, 12, 1, 22, 15).timestamp()
    result = end_of_minute(date)
    assert result == datetime(2014, 12, 1, 22, 15, 59, 999999)

def test_does_not_mutate_original_date():
    date = datetime(2014, 12, 1, 22, 15)
    end_of_minute(date)
    assert date == datetime(2014, 12, 1, 22, 15)

def test_returns_invalid_date_if_date_is_invalid():
    result = end_of_minute(float('nan'))
    with pytest.raises(ValueError):
        result.year  # Accessing any attribute should raise ValueError