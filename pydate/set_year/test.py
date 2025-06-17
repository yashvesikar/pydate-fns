
import pytest
from datetime import datetime
import math
from .set_year import set_year


def test_set_year_basic():
    """Test basic year setting"""
    result = set_year(datetime(2014, 9, 1), 2013)
    assert result == datetime(2013, 9, 1)
    
    result = set_year(datetime(2014, 9, 15, 11, 55, 0), 2020)
    assert result == datetime(2020, 9, 15, 11, 55, 0)


def test_set_year_preserves_time():
    """Test that time components are preserved"""
    result = set_year(datetime(2014, 9, 1, 11, 55, 59), 2018)
    assert result == datetime(2018, 9, 1, 11, 55, 59)


def test_set_year_with_timestamp():
    """Test set_year with timestamp input"""
    dt = datetime(2014, 8, 15)
    result = set_year(dt.timestamp(), 2019)
    assert result == datetime(2019, 8, 15)


def test_set_year_leap_year_adjustment():
    """Test February 29 adjustment when moving from leap year to non-leap year"""
    # February 29, 2016 (leap year) → 2015 (non-leap year) = February 28, 2015
    result = set_year(datetime(2016, 2, 29), 2015)
    assert result == datetime(2015, 2, 28)
    
    # February 29, 2016 (leap year) → 2017 (non-leap year) = February 28, 2017
    result = set_year(datetime(2016, 2, 29), 2017)
    assert result == datetime(2017, 2, 28)


def test_set_year_leap_year_to_leap_year():
    """Test February 29 preserved when moving from leap year to leap year"""
    # February 29, 2016 (leap year) → 2020 (leap year) = February 29, 2020
    result = set_year(datetime(2016, 2, 29), 2020)
    assert result == datetime(2020, 2, 29)
    
    # February 29, 2016 (leap year) → 2000 (leap year) = February 29, 2000
    result = set_year(datetime(2016, 2, 29), 2000)
    assert result == datetime(2000, 2, 29)


def test_set_year_century_years():
    """Test century years (special leap year rules)"""
    # 1900 is not a leap year (divisible by 100 but not 400)
    result = set_year(datetime(2016, 2, 29), 1900)
    assert result == datetime(1900, 2, 28)
    
    # 2000 is a leap year (divisible by 400)
    result = set_year(datetime(2016, 2, 29), 2000)
    assert result == datetime(2000, 2, 29)


def test_set_year_extreme_years():
    """Test with extreme year values"""
    # Very old year
    result = set_year(datetime(2014, 6, 15), 1)
    assert result == datetime(1, 6, 15)
    
    # Very new year
    result = set_year(datetime(2014, 6, 15), 9999)
    assert result == datetime(9999, 6, 15)


def test_set_year_negative_years():
    """Test with negative years"""
    # Note: Python datetime doesn't support years < 1, this should raise ValueError
    with pytest.raises(ValueError):
        set_year(datetime(2014, 6, 15), 0)
    
    with pytest.raises(ValueError):
        set_year(datetime(2014, 6, 15), -1)


def test_set_year_nan_year():
    """Test with NaN year returns invalid date"""
    result = set_year(datetime(2014, 9, 1), float('nan'))
    assert math.isnan(result.timestamp())


def test_set_year_invalid_input():
    """Test with invalid date input"""
    with pytest.raises(ValueError):
        set_year(float('nan'), 2020)


def test_set_year_does_not_mutate():
    """Test that the original date is not mutated"""
    date = datetime(2014, 9, 1)
    set_year(date, 2020)
    assert date == datetime(2014, 9, 1)
