from datetime import datetime
import math
from .difference_in_months import difference_in_months

def test_returns_number_of_full_months_between_dates():
    result = difference_in_months(
        datetime(2012, 7, 2, 18, 0),
        datetime(2011, 7, 2, 6, 0)
    )
    assert result == 12

def test_returns_negative_number_if_first_date_is_smaller():
    result = difference_in_months(
        datetime(2011, 7, 2, 6, 0),
        datetime(2012, 7, 2, 18, 0)
    )
    assert result == -12

def test_accepts_timestamps():
    result = difference_in_months(
        datetime(2014, 8, 2).timestamp(),
        datetime(2010, 7, 2).timestamp()
    )
    assert result == 49

def test_returns_diff_of_1_month_between_feb_28_and_jan_30():
    result = difference_in_months(
        datetime(2021, 2, 28),
        datetime(2021, 1, 30)
    )
    assert result == 1

def test_returns_diff_of_1_month_between_feb_28_and_jan_31():
    result = difference_in_months(
        datetime(2021, 2, 28),
        datetime(2021, 1, 31)
    )
    assert result == 1

def test_returns_diff_of_1_month_between_nov_30_and_oct_31():
    result = difference_in_months(
        datetime(2021, 11, 30),
        datetime(2021, 10, 31)
    )
    assert result == 1

def test_returns_diff_of_1_month_between_oct_31_and_sep_30():
    result = difference_in_months(
        datetime(2021, 10, 31),
        datetime(2021, 9, 30)
    )
    assert result == 1

def test_returns_diff_of_6_months_between_oct_31_and_apr_30():
    result = difference_in_months(
        datetime(2021, 10, 31),
        datetime(2021, 4, 30)
    )
    assert result == 6

def test_returns_diff_of_minus_1_month_between_sep_30_and_oct_31():
    result = difference_in_months(
        datetime(2021, 9, 30),
        datetime(2021, 10, 31)
    )
    assert result == -1

def test_less_than_month_different_calendar_months():
    result = difference_in_months(
        datetime(2014, 8, 1),
        datetime(2014, 7, 31)
    )
    assert result == 0

def test_less_than_month_swapped_dates():
    result = difference_in_months(
        datetime(2014, 7, 31),
        datetime(2014, 8, 1)
    )
    assert result == 0

def test_same_days_of_months():
    result = difference_in_months(
        datetime(2014, 9, 6),
        datetime(2014, 8, 6)
    )
    assert result == 1

def test_same_dates():
    result = difference_in_months(
        datetime(2014, 9, 5, 0, 0),
        datetime(2014, 9, 5, 0, 0)
    )
    assert result == 0

def test_does_not_return_negative_zero():
    result = difference_in_months(
        datetime(2014, 9, 5, 0, 0),
        datetime(2014, 9, 5, 0, 0)
    )
    assert not math.copysign(1, result) < 0  # Check it's not -0.0

def test_returns_nan_for_invalid_first_date():
    result = difference_in_months(
        float('nan'),
        datetime(2017, 1, 1)
    )
    assert math.isnan(result)

def test_returns_nan_for_invalid_second_date():
    result = difference_in_months(
        datetime(2017, 1, 1),
        float('nan')
    )
    assert math.isnan(result)

def test_returns_nan_for_both_invalid_dates():
    result = difference_in_months(
        float('nan'),
        float('nan')
    )
    assert math.isnan(result)