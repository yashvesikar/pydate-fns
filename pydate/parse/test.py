
import pytest
from datetime import datetime
from .parse import parse


def test_parse_basic_date_formats():
    """Test basic date format parsing"""
    reference = datetime(2020, 1, 1)
    
    # ISO format
    assert parse('2014-02-11', 'yyyy-MM-dd', reference) == datetime(2014, 2, 11, 0, 0)
    
    # US format
    assert parse('02/11/2014', 'MM/dd/yyyy', reference) == datetime(2014, 2, 11, 0, 0)
    
    # Short year format
    assert parse('02/11/14', 'MM/dd/yy', reference) == datetime(2014, 2, 11, 0, 0)
    
    # Single digit values
    assert parse('2/1/2014', 'M/d/yyyy', reference) == datetime(2014, 2, 1, 0, 0)


def test_parse_time_formats():
    """Test time format parsing"""
    reference = datetime(2020, 1, 1)
    
    # 24-hour format
    assert parse('15:30:45', 'HH:mm:ss', reference) == datetime(2020, 1, 1, 15, 30, 45)
    assert parse('1:5:9', 'H:m:s', reference) == datetime(2020, 1, 1, 1, 5, 9)
    
    # 12-hour format with AM/PM
    assert parse('3:30 PM', 'h:mm a', reference) == datetime(2020, 1, 1, 15, 30, 0)
    assert parse('12:00 AM', 'h:mm a', reference) == datetime(2020, 1, 1, 0, 0, 0)
    assert parse('12:00 PM', 'h:mm a', reference) == datetime(2020, 1, 1, 12, 0, 0)


def test_parse_datetime_combinations():
    """Test combined date and time parsing"""
    reference = datetime(2020, 1, 1)
    
    # Full datetime
    assert parse('2014-02-11 15:30:45', 'yyyy-MM-dd HH:mm:ss', reference) == datetime(2014, 2, 11, 15, 30, 45)
    
    # With 12-hour format
    assert parse('02/11/2014 3:30 PM', 'MM/dd/yyyy h:mm a', reference) == datetime(2014, 2, 11, 15, 30, 0)


def test_parse_month_names():
    """Test parsing with month names"""
    reference = datetime(2020, 1, 1)
    
    # Short month names
    assert parse('Feb 11, 2014', 'MMM dd, yyyy', reference) == datetime(2014, 2, 11, 0, 0)
    
    # Long month names
    assert parse('February 11, 2014', 'MMMM dd, yyyy', reference) == datetime(2014, 2, 11, 0, 0)


def test_parse_milliseconds():
    """Test parsing with milliseconds"""
    reference = datetime(2020, 1, 1)
    
    assert parse('15:30:45.123', 'HH:mm:ss.SSS', reference) == datetime(2020, 1, 1, 15, 30, 45, 123000)


def test_parse_two_digit_year_conversion():
    """Test 2-digit year conversion logic"""
    reference = datetime(2020, 1, 1)
    
    # Years 00-49 should map to 2000-2049
    assert parse('01/01/00', 'MM/dd/yy', reference) == datetime(2000, 1, 1, 0, 0)
    assert parse('01/01/49', 'MM/dd/yy', reference) == datetime(2049, 1, 1, 0, 0)
    
    # Years 50-99 should map to 1950-1999
    assert parse('01/01/50', 'MM/dd/yy', reference) == datetime(1950, 1, 1, 0, 0)
    assert parse('01/01/99', 'MM/dd/yy', reference) == datetime(1999, 1, 1, 0, 0)


def test_parse_quoted_literals():
    """Test parsing with quoted literal text"""
    reference = datetime(2020, 1, 1)
    
    assert parse("Today is Feb 11", "'Today is' MMM dd", reference) == datetime(2020, 2, 11, 0, 0)


def test_parse_reference_date():
    """Test how reference date is used for missing components"""
    reference = datetime(2023, 5, 15, 10, 30, 45)
    
    # Only time provided, should use reference date
    result = parse('15:30:45', 'HH:mm:ss', reference)
    assert result == datetime(2023, 5, 15, 15, 30, 45)
    
    # Only date provided, should reset time to 00:00:00
    result = parse('2014-02-11', 'yyyy-MM-dd', reference)
    assert result == datetime(2014, 2, 11, 0, 0, 0)


def test_parse_invalid_format():
    """Test parsing with invalid format strings"""
    reference = datetime(2020, 1, 1)
    
    with pytest.raises(ValueError, match="does not match format"):
        parse('2014/02/11', 'yyyy-MM-dd', reference)
    
    with pytest.raises(ValueError, match="does not match format"):
        parse('invalid', 'yyyy-MM-dd', reference)


def test_parse_invalid_date_components():
    """Test parsing with invalid date component values"""
    reference = datetime(2020, 1, 1)
    
    with pytest.raises(ValueError, match="Invalid month"):
        parse('2014-13-11', 'yyyy-MM-dd', reference)
    
    with pytest.raises(ValueError, match="Invalid day"):
        parse('2014-02-32', 'yyyy-MM-dd', reference)
    
    with pytest.raises(ValueError, match="Invalid hour"):
        parse('25:30:45', 'HH:mm:ss', reference)


def test_parse_edge_cases():
    """Test edge cases"""
    reference = datetime(2020, 1, 1)
    
    # Leap year
    assert parse('2020-02-29', 'yyyy-MM-dd', reference) == datetime(2020, 2, 29, 0, 0)
    
    # End of year
    assert parse('2014-12-31', 'yyyy-MM-dd', reference) == datetime(2014, 12, 31, 0, 0)
