
import pytest
from datetime import datetime, timezone, timedelta
from .parse_iso import parse_iso


def test_basic_iso_format():
    """Test basic ISO 8601 date string parsing."""
    result = parse_iso('2014-02-11T11:30:30')
    expected = datetime(2014, 2, 11, 11, 30, 30)
    assert result == expected


def test_iso_with_utc_timezone():
    """Test ISO string with UTC timezone marker."""
    result = parse_iso('2014-02-11T11:30:30Z')
    expected = datetime(2014, 2, 11, 11, 30, 30, tzinfo=timezone.utc)
    assert result == expected


def test_iso_with_timezone_offset():
    """Test ISO string with timezone offset."""
    result = parse_iso('2014-02-11T13:46:20+07:00')
    expected = datetime(2014, 2, 11, 13, 46, 20, tzinfo=timezone(timedelta(hours=7)))
    assert result == expected


def test_iso_with_negative_timezone_offset():
    """Test ISO string with negative timezone offset."""
    result = parse_iso('2014-02-11T13:46:20-05:00')
    expected = datetime(2014, 2, 11, 13, 46, 20, tzinfo=timezone(timedelta(hours=-5)))
    assert result == expected


def test_date_only():
    """Test date-only ISO strings."""
    # Year only
    result = parse_iso('2014')
    expected = datetime(2014, 1, 1)
    assert result == expected
    
    # Year-month
    result = parse_iso('2014-02')
    expected = datetime(2014, 2, 1)
    assert result == expected
    
    # Full date
    result = parse_iso('2014-02-11')
    expected = datetime(2014, 2, 11)
    assert result == expected


def test_week_date_format():
    """Test ISO week date format parsing."""
    # Week only (defaults to Monday)
    result = parse_iso('2014-W02')
    expected = datetime(2014, 1, 6)  # Monday of week 2
    assert result == expected
    
    # Week with weekday
    result = parse_iso('2014-W02-7')
    expected = datetime(2014, 1, 12)  # Sunday of week 2
    assert result == expected
    
    # First week of year
    result = parse_iso('2009-W01-1')
    expected = datetime(2008, 12, 29)  # Monday of week 1 (in previous year)
    assert result == expected


def test_ordinal_date_format():
    """Test ordinal date format parsing."""
    result = parse_iso('2014-026')
    expected = datetime(2014, 1, 26)  # 26th day of year
    assert result == expected
    
    # Leap year ordinal date
    result = parse_iso('2016-060')
    expected = datetime(2016, 2, 29)  # 60th day of leap year (Feb 29)
    assert result == expected


def test_time_components():
    """Test various time component formats."""
    # Hours only
    result = parse_iso('2014-02-11T11')
    expected = datetime(2014, 2, 11, 11, 0, 0)
    assert result == expected
    
    # Hours and minutes
    result = parse_iso('2014-02-11T11:30')
    expected = datetime(2014, 2, 11, 11, 30, 0)
    assert result == expected
    
    # Full time
    result = parse_iso('2014-02-11T11:30:30')
    expected = datetime(2014, 2, 11, 11, 30, 30)
    assert result == expected
    
    # With milliseconds
    result = parse_iso('2014-02-11T11:30:30.768')
    expected = datetime(2014, 2, 11, 11, 30, 30, 768000)
    assert result == expected


def test_fractional_time():
    """Test fractional time components."""
    # Fractional hours
    result = parse_iso('2014-02-11T11.5')
    expected = datetime(2014, 2, 11, 11, 30, 0)
    assert result == expected
    
    # Fractional minutes
    result = parse_iso('2014-02-11T11:30.5')
    expected = datetime(2014, 2, 11, 11, 30, 30)
    assert result == expected
    
    # Fractional seconds
    result = parse_iso('2014-02-11T11:30:30.25')
    expected = datetime(2014, 2, 11, 11, 30, 30, 250000)
    assert result == expected


def test_24_hour_format():
    """Test 24:00 hour format (midnight of next day)."""
    result = parse_iso('2014-02-11T24:00:00')
    expected = datetime(2014, 2, 12, 0, 0, 0)  # Next day at midnight
    assert result == expected


def test_compact_formats():
    """Test compact ISO formats without separators."""
    # Compact date
    result = parse_iso('20140211')
    expected = datetime(2014, 2, 11)
    assert result == expected
    
    # Compact datetime
    result = parse_iso('20140211T113030')
    expected = datetime(2014, 2, 11, 11, 30, 30)
    assert result == expected


def test_timezone_variations():
    """Test various timezone format variations."""
    # Without colon separator
    result = parse_iso('2014-02-11T11:30:30+0700')
    expected = datetime(2014, 2, 11, 11, 30, 30, tzinfo=timezone(timedelta(hours=7)))
    assert result == expected
    
    # Hour-only offset
    result = parse_iso('2014-02-11T11:30:30+07')
    expected = datetime(2014, 2, 11, 11, 30, 30, tzinfo=timezone(timedelta(hours=7)))
    assert result == expected


def test_extended_year_format():
    """Test extended year format."""
    # Positive extended year (within Python's datetime range)
    result = parse_iso('+001234-07-02')
    expected = datetime(1234, 7, 2)
    assert result == expected
    
    # Note: Negative years are not supported by Python's datetime


def test_leap_year_handling():
    """Test leap year date handling."""
    # Valid leap year date
    result = parse_iso('2016-02-29')
    expected = datetime(2016, 2, 29)
    assert result == expected
    
    # Invalid non-leap year date should raise error
    with pytest.raises(ValueError):
        parse_iso('2015-02-29')


def test_invalid_dates():
    """Test various invalid date formats."""
    invalid_dates = [
        '',  # Empty string
        'abc',  # Non-date string
        '2014-13-01',  # Invalid month
        '2014-02-30',  # Invalid day for month
        '2014-02-11T25:00',  # Invalid hour
        '2014-02-11T11:60',  # Invalid minute
        '2014-02-11T11:30:60',  # Invalid second
        '2014-W54',  # Invalid week number
        '2014-W02-8',  # Invalid weekday
        '2014-367',  # Invalid day of year
        '2014-02-11T24:01',  # Invalid 24:xx time
        '2014-02-11T11:30:30+25:00',  # Invalid timezone offset
    ]
    
    for invalid_date in invalid_dates:
        with pytest.raises(ValueError):
            parse_iso(invalid_date)


def test_non_string_input():
    """Test that non-string input raises ValueError."""
    with pytest.raises(ValueError, match="Date string must be a string"):
        parse_iso(123)  # type: ignore
    
    with pytest.raises(ValueError, match="Date string must be a string"):
        parse_iso(None)  # type: ignore


def test_edge_cases():
    """Test edge cases and boundary conditions."""
    # Minimum valid date (Python datetime starts from year 1)
    result = parse_iso('0001-01-01')
    expected = datetime(1, 1, 1)
    assert result == expected
    
    # December 31st
    result = parse_iso('2014-12-31')
    expected = datetime(2014, 12, 31)
    assert result == expected
    
    # Last day of leap year
    result = parse_iso('2016-12-31')
    expected = datetime(2016, 12, 31)
    assert result == expected
    
    # Week 53 (rare but valid)
    result = parse_iso('2009-W53-7')
    expected = datetime(2010, 1, 3)  # Sunday of week 53
    assert result == expected


def test_iso_week_calculations():
    """Test ISO week date calculations."""
    # Test that week 1 contains January 4th
    result = parse_iso('2014-W01-1')  # Monday of week 1
    jan4_2014 = datetime(2014, 1, 4)  # Saturday
    # Week 1 should contain Jan 4, so Monday should be Dec 30, 2013
    expected = datetime(2013, 12, 30)
    assert result == expected
    
    # Test week boundaries around new year
    result = parse_iso('2014-W01-6')  # Saturday of week 1 (should be Jan 4)
    expected = datetime(2014, 1, 4)
    assert result == expected


def test_ordinal_date_leap_year():
    """Test ordinal dates in leap years."""
    # Day 60 in leap year (Feb 29)
    result = parse_iso('2016-060')
    expected = datetime(2016, 2, 29)
    assert result == expected
    
    # Day 366 in leap year (Dec 31)
    result = parse_iso('2016-366')
    expected = datetime(2016, 12, 31)
    assert result == expected
    
    # Day 366 in non-leap year should fail
    with pytest.raises(ValueError):
        parse_iso('2015-366')


def test_comma_decimal_separator():
    """Test comma as decimal separator (European format)."""
    result = parse_iso('2014-02-11T11:30:30,768')
    expected = datetime(2014, 2, 11, 11, 30, 30, 768000)
    assert result == expected
    
    result = parse_iso('2014-02-11T11,5')
    expected = datetime(2014, 2, 11, 11, 30, 0)
    assert result == expected
