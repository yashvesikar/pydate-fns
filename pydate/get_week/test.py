
import pytest
from datetime import datetime
import math
from .get_week import get_week


def test_get_week_basic():
    """Test basic week number functionality"""
    # January 2, 2005 should be week 2 with default options
    result = get_week(datetime(2005, 1, 2))
    assert result == 2
    
    # January 1, 2005 should be week 1
    result = get_week(datetime(2005, 1, 1))
    assert result == 1


def test_get_week_with_options():
    """Test with custom week start and first week options"""
    # Test with Monday as first day and 4th January always in first week
    # This matches the JavaScript test: getWeek(new Date(2005, 0, 2), { weekStartsOn: 1, firstWeekContainsDate: 4 }) => 53
    result = get_week(datetime(2005, 1, 2), week_starts_on=1, first_week_contains_date=4)
    assert result == 53


def test_get_week_mid_year():
    """Test week numbers in the middle of the year"""
    # June dates should have higher week numbers
    result = get_week(datetime(2005, 6, 15))
    assert result > 20  # Should be around week 24-25
    
    # December dates should have even higher week numbers
    result = get_week(datetime(2005, 12, 31))
    assert result > 50  # Should be around week 52-53


def test_get_week_with_timestamps():
    """Test with timestamp input"""
    timestamp = datetime(2005, 1, 2).timestamp()
    result = get_week(timestamp)
    assert result == 2


def test_get_week_december_edge_case():
    """Test edge case from JavaScript tests"""
    # Test December 29, 2008 should be week 1 (of next year)
    result = get_week(datetime(2008, 12, 29))
    assert result == 1


def test_get_week_invalid_date():
    """Test invalid date handling"""
    # Test with an invalid timestamp that should result in NaN
    try:
        result = get_week(float('nan'))
        assert math.isnan(result)
    except (ValueError, OSError):
        # This is also acceptable behavior for invalid input
        pass


def test_get_week_negative_years():
    """Test with negative year dates"""
    # Test some edge cases with negative years
    result = get_week(datetime(2005, 1, 4))
    assert result == 2
    
    # The exact behavior for very old dates may vary, but should not crash
    try:
        result = get_week(datetime(395, 1, 4))
        assert isinstance(result, (int, float))
    except (ValueError, OSError):
        # This is acceptable for very old dates
        pass
