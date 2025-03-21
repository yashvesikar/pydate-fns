from datetime import datetime
import pytest
from .end_of_second import end_of_second

def test_returns_date_with_time_set_to_last_millisecond_before_second_ends():
    date = datetime(2014, 12, 1, 22, 15, 30)
    result = end_of_second(date)
    assert result == datetime(2014, 12, 1, 22, 15, 30, 999999)

def test_accepts_timestamp():
    date = datetime(2014, 12, 1, 22, 15, 45).timestamp()
    result = end_of_second(date)
    assert result == datetime(2014, 12, 1, 22, 15, 45, 999999)

def test_does_not_mutate_original_date():
    date = datetime(2014, 12, 1, 22, 15, 15, 300)
    end_of_second(date)
    assert date == datetime(2014, 12, 1, 22, 15, 15, 300)

def test_returns_invalid_date_if_date_is_invalid():
    result = end_of_second(float('nan'))
    with pytest.raises(ValueError):
        result.year  # Accessing any attribute should raise ValueError