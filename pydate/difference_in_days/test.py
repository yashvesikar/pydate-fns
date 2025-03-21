from datetime import datetime
import math
from .difference_in_days import difference_in_days

def test_returns_number_of_full_days_between_dates():
    result = difference_in_days(
        datetime(2012, 7, 2, 18, 0),
        datetime(2011, 7, 2, 6, 0)
    )
    assert result == 366

def test_returns_negative_number_if_first_date_is_smaller():
    result = difference_in_days(
        datetime(2011, 7, 2, 6, 0),
        datetime(2012, 7, 2, 18, 0)
    )
    assert result == -366

def test_accepts_timestamps():
    result = difference_in_days(
        datetime(2014, 9, 5, 18, 0).timestamp(),
        datetime(2014, 9, 4, 6, 0).timestamp()
    )
    assert result == 1

def test_less_than_day_different_calendar_days():
    result = difference_in_days(
        datetime(2014, 9, 5, 0, 0),
        datetime(2014, 9, 4, 23, 59)
    )
    assert result == 0

def test_less_than_day_swapped_dates():
    result = difference_in_days(
        datetime(2014, 9, 4, 23, 59),
        datetime(2014, 9, 5, 0, 0)
    )
    assert result == 0

def test_same_time_values():
    result = difference_in_days(
        datetime(2014, 9, 6, 0, 0),
        datetime(2014, 9, 5, 0, 0)
    )
    assert result == 1

def test_same_dates():
    result = difference_in_days(
        datetime(2014, 9, 5, 0, 0),
        datetime(2014, 9, 5, 0, 0)
    )
    assert result == 0

def test_does_not_return_negative_zero():
    result = difference_in_days(
        datetime(2014, 9, 5, 0, 0),
        datetime(2014, 9, 5, 0, 0)
    )
    assert not math.copysign(1, result) < 0  # Check it's not -0.0

def test_returns_nan_for_invalid_first_date():
    result = difference_in_days(
        float('nan'),
        datetime(2017, 1, 1)
    )
    assert math.isnan(result)

def test_returns_nan_for_invalid_second_date():
    result = difference_in_days(
        datetime(2017, 1, 1),
        float('nan')
    )
    assert math.isnan(result)

def test_returns_nan_for_both_invalid_dates():
    result = difference_in_days(
        float('nan'),
        float('nan')
    )
    assert math.isnan(result)