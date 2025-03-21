from datetime import datetime
import math
from .difference_in_minutes import difference_in_minutes

def test_returns_number_of_minutes_between_dates():
    result = difference_in_minutes(
        datetime(2014, 7, 2, 12, 20),
        datetime(2014, 7, 2, 12, 6)
    )
    assert result == 14

def test_returns_number_of_minutes_with_default_rounding_method():
    result = difference_in_minutes(
        datetime(2014, 7, 2, 12, 6, 50),
        datetime(2014, 7, 2, 12, 20, 10)
    )
    assert result == -13

def test_returns_number_of_minutes_with_trunc_rounding_method():
    result = difference_in_minutes(
        datetime(2014, 7, 2, 12, 20, 50),
        datetime(2014, 7, 2, 12, 6, 10),
        rounding_method="trunc"
    )
    assert result == 14

def test_returns_number_of_minutes_with_ceil_rounding_method():
    result = difference_in_minutes(
        datetime(2014, 7, 2, 12, 20, 50),
        datetime(2014, 7, 2, 12, 6, 10),
        rounding_method="ceil"
    )
    assert result == 15

def test_returns_number_of_minutes_with_floor_rounding_method():
    result = difference_in_minutes(
        datetime(2014, 7, 2, 12, 20, 50),
        datetime(2014, 7, 2, 12, 6, 10),
        rounding_method="floor"
    )
    assert result == 14

def test_returns_number_of_minutes_with_round_rounding_method():
    result = difference_in_minutes(
        datetime(2014, 7, 2, 12, 20, 50),  # Changed from 60 to 50 seconds
        datetime(2014, 7, 2, 12, 6, 10),
        rounding_method="round"
    )
    assert result == 15

def test_returns_negative_number_if_first_date_is_smaller():
    result = difference_in_minutes(
        datetime(2014, 7, 2, 12, 6),
        datetime(2014, 7, 2, 12, 20)
    )
    assert result == -14

def test_accepts_timestamps():
    result = difference_in_minutes(
        datetime(2014, 9, 5, 18, 45).timestamp(),
        datetime(2014, 9, 5, 18, 15).timestamp()
    )
    assert result == 30

def test_difference_less_than_minute_different_calendar_minutes():
    result = difference_in_minutes(
        datetime(2014, 9, 5, 12, 12),
        datetime(2014, 9, 5, 12, 11, 59)
    )
    assert result == 0

def test_difference_less_than_minute_swapped_dates():
    result = difference_in_minutes(
        datetime(2014, 9, 5, 12, 11, 59),
        datetime(2014, 9, 5, 12, 12)
    )
    assert result == 0

def test_difference_integral_number_of_minutes():
    result = difference_in_minutes(
        datetime(2014, 9, 5, 12, 25),
        datetime(2014, 9, 5, 12, 15)
    )
    assert result == 10

def test_same_dates():
    result = difference_in_minutes(
        datetime(2014, 9, 5, 0, 0),
        datetime(2014, 9, 5, 0, 0)
    )
    assert result == 0

def test_does_not_return_negative_zero():
    result = difference_in_minutes(
        datetime(2014, 9, 5, 0, 0),
        datetime(2014, 9, 5, 0, 0)
    )
    assert not math.copysign(1, result) < 0  # Check it's not -0.0

def test_returns_nan_for_invalid_first_date():
    result = difference_in_minutes(
        float('nan'),
        datetime(2017, 1, 1)
    )
    assert math.isnan(result)

def test_returns_nan_for_invalid_second_date():
    result = difference_in_minutes(
        datetime(2017, 1, 1),
        float('nan')
    )
    assert math.isnan(result)

def test_returns_nan_for_both_invalid_dates():
    result = difference_in_minutes(
        float('nan'),
        float('nan')
    )
    assert math.isnan(result)