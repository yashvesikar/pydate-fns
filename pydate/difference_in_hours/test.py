from datetime import datetime
import math
from .difference_in_hours import difference_in_hours

def test_returns_number_of_hours_with_default_rounding_method():
    result = difference_in_hours(
        datetime(2014, 7, 2, 6, 0, 29),
        datetime(2014, 7, 2, 20, 0, 28, 973000)
    )
    assert result == -13

def test_returns_number_of_hours_between_dates():
    result = difference_in_hours(
        datetime(2014, 7, 2, 20, 0),
        datetime(2014, 7, 2, 6, 0)
    )
    assert result == 14

def test_returns_negative_number_if_first_date_is_smaller():
    result = difference_in_hours(
        datetime(2014, 7, 2, 6, 0),
        datetime(2014, 7, 2, 20, 0)
    )
    assert result == -14

def test_returns_zero_not_negative_zero():
    result = difference_in_hours(
        datetime(2021, 7, 22, 6, 1, 28, 973000),
        datetime(2021, 7, 22, 6, 1, 28, 976000)
    )
    assert result == 0
    assert not math.copysign(1, result) < 0  # Check it's not -0.0

def test_returns_two_with_ceil_rounding():
    result = difference_in_hours(
        datetime(2021, 7, 22, 7, 1, 29, 976000),
        datetime(2021, 7, 22, 6, 1, 28, 173000),
        rounding_method="ceil"
    )
    assert result == 2

def test_returns_one_with_floor_rounding():
    result = difference_in_hours(
        datetime(2021, 7, 22, 7, 1, 29, 976000),
        datetime(2021, 7, 22, 6, 1, 28, 173000),
        rounding_method="floor"
    )
    assert result == 1

def test_returns_one_with_round_rounding():
    result = difference_in_hours(
        datetime(2021, 7, 22, 7, 1, 29, 976000),
        datetime(2021, 7, 22, 6, 1, 28, 173000),
        rounding_method="round"
    )
    assert result == 1

def test_returns_one_with_trunc_rounding():
    result = difference_in_hours(
        datetime(2021, 7, 22, 7, 1, 29, 976000),
        datetime(2021, 7, 22, 6, 1, 28, 173000),
        rounding_method="trunc"
    )
    assert result == 1

def test_accepts_timestamps():
    result = difference_in_hours(
        datetime(2014, 9, 5, 18, 0).timestamp(),
        datetime(2014, 9, 5, 6, 0).timestamp()
    )
    assert result == 12

def test_less_than_hour_different_calendar_hours():
    result = difference_in_hours(
        datetime(2014, 9, 5, 12, 0),
        datetime(2014, 9, 5, 11, 59)
    )
    assert result == 0

def test_less_than_hour_swapped_dates():
    result = difference_in_hours(
        datetime(2014, 9, 5, 11, 59),
        datetime(2014, 9, 5, 12, 0)
    )
    assert result == 0

def test_integral_number_of_hours():
    result = difference_in_hours(
        datetime(2014, 9, 5, 13, 0),
        datetime(2014, 9, 5, 12, 0)
    )
    assert result == 1

def test_same_dates():
    result = difference_in_hours(
        datetime(2014, 9, 5, 0, 0),
        datetime(2014, 9, 5, 0, 0)
    )
    assert result == 0

def test_does_not_return_negative_zero():
    result = difference_in_hours(
        datetime(2014, 9, 5, 0, 0),
        datetime(2014, 9, 5, 0, 0)
    )
    assert not math.copysign(1, result) < 0  # Check it's not -0.0

def test_returns_nan_for_invalid_first_date():
    result = difference_in_hours(
        float('nan'),
        datetime(2017, 1, 1)
    )
    assert math.isnan(result)

def test_returns_nan_for_invalid_second_date():
    result = difference_in_hours(
        datetime(2017, 1, 1),
        float('nan')
    )
    assert math.isnan(result)

def test_returns_nan_for_both_invalid_dates():
    result = difference_in_hours(
        float('nan'),
        float('nan')
    )
    assert math.isnan(result)