from datetime import datetime
import pytest
from .start_of_second import start_of_second

def test_returns_date_with_time_set_to_first_millisecond_of_second():
    date = datetime(2014, 12, 1, 22, 15, 45, 400000)
    result = start_of_second(date)
    assert result == datetime(2014, 12, 1, 22, 15, 45)

def test_accepts_timestamp():
    date = datetime(2014, 12, 1, 22, 15, 45, 400000).timestamp()
    result = start_of_second(date)
    assert result == datetime(2014, 12, 1, 22, 15, 45)

def test_does_not_mutate_original_date():
    date = datetime(2014, 12, 1, 22, 15, 45, 400000)
    start_of_second(date)
    assert date == datetime(2014, 12, 1, 22, 15, 45, 400000)

def test_returns_invalid_date_if_date_is_invalid():
    result = start_of_second(float('nan'))
    with pytest.raises(ValueError):
        result.year  # Accessing any attribute should raise ValueError