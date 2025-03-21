from datetime import datetime
import math
from .difference_in_calendar_years import difference_in_calendar_years

def test_returns_number_of_calendar_years_between_dates():
    result = difference_in_calendar_years(
        datetime(2012, 7, 2, 18, 0),
        datetime(2011, 7, 2, 6, 0)
    )
    assert result == 1

def test_returns_negative_number_if_first_date_is_smaller():
    result = difference_in_calendar_years(
        datetime(2011, 7, 2, 6, 0),
        datetime(2012, 7, 2, 18, 0)
    )
    assert result == -1

def test_accepts_timestamps():
    result = difference_in_calendar_years(
        datetime(2014, 7, 2).timestamp(),
        datetime(2010, 7, 2).timestamp()
    )
    assert result == 4

def test_less_than_year_different_calendar_years():
    result = difference_in_calendar_years(
        datetime(2015, 1, 1),
        datetime(2014, 12, 31)
    )
    assert result == 1

def test_less_than_year_swapped_dates():
    result = difference_in_calendar_years(
        datetime(2014, 12, 31),
        datetime(2015, 1, 1)
    )
    assert result == -1

def test_same_days_and_months():
    result = difference_in_calendar_years(
        datetime(2014, 9, 5),
        datetime(2012, 9, 5)
    )
    assert result == 2

def test_same_dates():
    result = difference_in_calendar_years(
        datetime(2014, 9, 5, 0, 0),
        datetime(2014, 9, 5, 0, 0)
    )
    assert result == 0

def test_does_not_return_negative_zero():
    result = difference_in_calendar_years(
        datetime(2014, 9, 5, 0, 0),
        datetime(2014, 9, 5, 0, 0)
    )
    assert not math.copysign(1, result) < 0  # Check it's not -0.0

def test_returns_nan_for_invalid_first_date():
    result = difference_in_calendar_years(
        float('nan'),
        datetime(2017, 1, 1)
    )
    assert math.isnan(result)

def test_returns_nan_for_invalid_second_date():
    result = difference_in_calendar_years(
        datetime(2017, 1, 1),
        float('nan')
    )
    assert math.isnan(result)

def test_returns_nan_for_both_invalid_dates():
    result = difference_in_calendar_years(
        float('nan'),
        float('nan')
    )
    assert math.isnan(result)