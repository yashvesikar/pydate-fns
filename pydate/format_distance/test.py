
import pytest
from datetime import datetime, timedelta
from .format_distance import format_distance


def test_format_distance_seconds():
    """Test distance formatting for seconds"""
    base = datetime(2015, 1, 1, 0, 0, 0)
    
    # Less than a minute
    assert format_distance(base + timedelta(seconds=0), base) == "less than a minute"
    assert format_distance(base + timedelta(seconds=25), base) == "less than a minute"
    
    # With includeSeconds
    assert format_distance(base + timedelta(seconds=2), base, {'includeSeconds': True}) == "less than 5 seconds"
    assert format_distance(base + timedelta(seconds=7), base, {'includeSeconds': True}) == "less than 10 seconds"
    assert format_distance(base + timedelta(seconds=15), base, {'includeSeconds': True}) == "less than 20 seconds"
    assert format_distance(base + timedelta(seconds=25), base, {'includeSeconds': True}) == "half a minute"
    assert format_distance(base + timedelta(seconds=45), base, {'includeSeconds': True}) == "less than a minute"
    assert format_distance(base + timedelta(seconds=65), base, {'includeSeconds': True}) == "1 minute"


def test_format_distance_minutes():
    """Test distance formatting for minutes"""
    base = datetime(2015, 1, 1, 0, 0, 0)
    
    # 1 minute
    assert format_distance(base + timedelta(seconds=45), base) == "1 minute"
    assert format_distance(base + timedelta(seconds=89), base) == "1 minute"
    
    # X minutes
    assert format_distance(base + timedelta(minutes=2), base) == "2 minutes"
    assert format_distance(base + timedelta(minutes=44), base) == "44 minutes"


def test_format_distance_hours():
    """Test distance formatting for hours"""
    base = datetime(2015, 1, 1, 0, 0, 0)
    
    # About 1 hour
    assert format_distance(base + timedelta(minutes=45), base) == "about 1 hour"
    assert format_distance(base + timedelta(minutes=89), base) == "about 1 hour"
    
    # About X hours
    assert format_distance(base + timedelta(minutes=90), base) == "about 2 hours"
    assert format_distance(base + timedelta(hours=23), base) == "about 23 hours"


def test_format_distance_days():
    """Test distance formatting for days"""
    base = datetime(2015, 1, 1, 0, 0, 0)
    
    # 1 day
    assert format_distance(base + timedelta(hours=24), base) == "1 day"
    assert format_distance(base + timedelta(hours=41), base) == "1 day"
    
    # X days
    assert format_distance(base + timedelta(hours=42), base) == "2 days"
    assert format_distance(base + timedelta(days=29), base) == "29 days"


def test_format_distance_months():
    """Test distance formatting for months"""
    base = datetime(2015, 1, 1)
    
    # About 1 month
    assert format_distance(base + timedelta(days=32), base) == "about 1 month"
    
    # X months
    assert format_distance(datetime(2015, 7, 2), datetime(2015, 1, 1)) == "6 months"
    assert format_distance(datetime(2015, 12, 1), datetime(2015, 1, 1)) == "11 months"


def test_format_distance_years():
    """Test distance formatting for years"""
    base = datetime(2015, 1, 1)
    
    # About 1 year
    assert format_distance(datetime(2016, 1, 1), base) == "about 1 year"
    assert format_distance(datetime(2016, 3, 1), base) == "about 1 year"
    
    # Over 1 year
    assert format_distance(datetime(2016, 6, 1), base) == "over 1 year"
    
    # Almost 2 years
    assert format_distance(datetime(2016, 11, 1), base) == "almost 2 years"
    
    # Multiple years
    assert format_distance(datetime(2020, 1, 1), base) == "about 5 years"


def test_format_distance_with_suffix():
    """Test distance formatting with suffix"""
    base = datetime(2015, 1, 1)
    
    # Past
    assert format_distance(base, datetime(2016, 1, 1), {'addSuffix': True}) == "about 1 year ago"
    assert format_distance(base, base + timedelta(days=3), {'addSuffix': True}) == "3 days ago"
    
    # Future
    assert format_distance(datetime(2016, 1, 1), base, {'addSuffix': True}) == "in about 1 year"
    assert format_distance(base + timedelta(days=3), base, {'addSuffix': True}) == "in 3 days"


def test_format_distance_edge_cases():
    """Test edge cases"""
    base = datetime(2015, 1, 1)
    
    # Same dates
    assert format_distance(base, base) == "less than a minute"
    
    # Order doesn't matter
    assert format_distance(base, base + timedelta(days=5)) == format_distance(base + timedelta(days=5), base)


def test_format_distance_with_timestamps():
    """Test with timestamp inputs"""
    base_timestamp = 1420070400  # 2015-01-01 00:00:00 UTC
    later_timestamp = 1420070400 + 3600  # 1 hour later
    
    result = format_distance(later_timestamp, base_timestamp)
    assert result == "about 1 hour"


def test_format_distance_invalid_dates():
    """Test with invalid dates"""
    with pytest.raises(ValueError, match="Invalid time value"):
        format_distance(float('nan'), datetime(2015, 1, 1))
    
    with pytest.raises(ValueError, match="Invalid time value"):
        format_distance(datetime(2015, 1, 1), float('nan'))
