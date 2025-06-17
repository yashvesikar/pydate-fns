
from datetime import datetime, timezone, timedelta
import re
import math
from typing import Union, Optional
from ..to_date.to_date import to_date


def parse_iso(date_string: str, additional_digits: int = 2) -> datetime:
    """
    Parse ISO 8601 date string and return a datetime object.
    
    Args:
        date_string: ISO 8601 formatted date string
        additional_digits: Number of additional digits in extended year format (0, 1, or 2)
        
    Returns:
        datetime: Parsed datetime object
        
    Raises:
        ValueError: If the date string is invalid or cannot be parsed
    
    Examples:
        >>> parse_iso('2014-02-11T11:30:30')  # Basic ISO format
        datetime(2014, 2, 11, 11, 30, 30)
        
        >>> parse_iso('2014-02-11T11:30:30Z')  # UTC timezone
        datetime(2014, 2, 11, 11, 30, 30, tzinfo=timezone.utc)
        
        >>> parse_iso('2014-02-11T13:46:20+07:00')  # With timezone offset
        datetime(2014, 2, 11, 13, 46, 20, tzinfo=timezone(timedelta(hours=7)))
        
        >>> parse_iso('2014-W02-7')  # Week date format
        datetime(2014, 1, 12)  # Sunday of week 2
        
        >>> parse_iso('2014-026')  # Ordinal date format
        datetime(2014, 1, 26)  # 26th day of year
    """
    if not isinstance(date_string, str):
        raise ValueError("Date string must be a string")
        
    if not date_string:
        raise ValueError("Date string cannot be empty")
    
    try:
        # Parse the input string into components
        date_part, time_part, timezone_part = _split_date_string(date_string)
        
        # Parse year and date components
        year, month, day = _parse_date_part(date_part, additional_digits)
        
        # Parse time components (default to midnight)
        hour, minute, second, microsecond = _parse_time_part(time_part) if time_part else (0, 0, 0, 0)
        
        # Parse timezone
        tz = _parse_timezone_part(timezone_part) if timezone_part else None
        
        # Handle special case of 24:00 (midnight of next day)
        if hour == 24:
            if minute != 0 or second != 0 or microsecond != 0:
                raise ValueError("Invalid time: 24:00 must have zero minutes and seconds")
            hour = 0
            # Add one day
            temp_date = datetime(year, month, day, hour, minute, second, microsecond, tz)
            temp_date = temp_date + timedelta(days=1)
            return temp_date
        
        return datetime(year, month, day, hour, minute, second, microsecond, tz)
        
    except (ValueError, TypeError, OverflowError) as e:
        raise ValueError(f"Invalid ISO 8601 date string: {date_string}") from e


def _split_date_string(date_string: str) -> tuple[str, Optional[str], Optional[str]]:
    """Split the date string into date, time, and timezone parts."""
    # Remove any whitespace
    date_string = date_string.strip()
    
    # First split date and time parts
    if 'T' in date_string:
        date_part, time_tz_part = date_string.split('T', 1)
        
        # Check for timezone info at the end of time part
        timezone_part = None
        time_part = time_tz_part
        
        if time_tz_part.endswith('Z'):
            timezone_part = 'Z'
            time_part = time_tz_part[:-1]
        else:
            # Look for timezone offset pattern at the end
            tz_match = re.search(r'([+-]\d{2}(?::?\d{2})?)$', time_tz_part)
            if tz_match:
                timezone_part = tz_match.group(1)
                time_part = time_tz_part[:tz_match.start()]
    else:
        date_part = date_string
        time_part = None
        timezone_part = None
    
    return date_part, time_part, timezone_part


def _parse_date_part(date_part: str, additional_digits: int) -> tuple[int, int, int]:
    """Parse the date part of the ISO string."""
    if not date_part:
        raise ValueError("Date part cannot be empty")
    
    # Handle extended year format
    if date_part.startswith(('+', '-')):
        return _parse_extended_year_date(date_part, additional_digits)
    
    # Handle different date formats
    if 'W' in date_part:
        return _parse_week_date(date_part)
    elif len(date_part) == 4:
        # Year only
        year = int(date_part)
        return year, 1, 1
    elif len(date_part) == 7 and date_part[4] == '-':
        # Year-Month
        year = int(date_part[:4])
        month = int(date_part[5:7])
        _validate_month(month)
        return year, month, 1
    elif len(date_part) == 8 and '-' not in date_part:
        # Compact date (YYYYMMDD)
        return _parse_calendar_date(date_part)
    elif len(date_part) == 7 and '-' not in date_part:
        # Ordinal date (YYYYDDD)
        return _parse_ordinal_date(date_part)
    elif len(date_part) == 8 and date_part[4] == '-':
        # Ordinal date with dash (YYYY-DDD)
        year = int(date_part[:4])
        day_of_year = int(date_part[5:8])
        max_days = 366 if _is_leap_year(year) else 365
        if day_of_year < 1 or day_of_year > max_days:
            raise ValueError(f"Day of year must be between 1 and {max_days} for year {year}")
        return _day_of_year_to_date(year, day_of_year)
    else:
        # Regular date format
        return _parse_calendar_date(date_part)


def _parse_extended_year_date(date_part: str, additional_digits: int) -> tuple[int, int, int]:
    """Parse extended year format dates."""
    sign = 1 if date_part[0] == '+' else -1
    
    # Extract year digits based on additional_digits
    year_digits = 4 + additional_digits
    year_str = date_part[1:1 + year_digits]
    
    if len(year_str) != year_digits:
        raise ValueError(f"Extended year must have {year_digits} digits")
    
    year = sign * int(year_str)
    
    # Parse the rest of the date
    remaining = date_part[1 + year_digits:]
    
    if not remaining:
        return year, 1, 1
    elif remaining.startswith('-'):
        remaining = remaining[1:]
        if len(remaining) == 2:
            month = int(remaining)
            _validate_month(month)
            return year, month, 1
        elif len(remaining) == 5 and remaining[2] == '-':
            month = int(remaining[:2])
            day = int(remaining[3:5])
            _validate_month(month)
            _validate_day(year, month, day)
            return year, month, day
    
    raise ValueError("Invalid extended year date format")


def _parse_week_date(date_part: str) -> tuple[int, int, int]:
    """Parse ISO week date format (YYYY-Www-d)."""
    parts = date_part.split('-')
    
    if len(parts) < 2 or not parts[1].startswith('W'):
        raise ValueError("Invalid week date format")
    
    year = int(parts[0])
    week_str = parts[1][1:]  # Remove 'W'
    week = int(week_str)
    
    if week < 1 or week > 53:
        raise ValueError(f"Week number must be between 1 and 53, got {week}")
    
    weekday = 1  # Monday by default
    if len(parts) == 3:
        weekday = int(parts[2])
        if weekday < 1 or weekday > 7:
            raise ValueError(f"Weekday must be between 1 and 7, got {weekday}")
    
    # Convert ISO week date to calendar date
    return _iso_week_to_date(year, week, weekday)


def _parse_ordinal_date(date_part: str) -> tuple[int, int, int]:
    """Parse ordinal date format (YYYYDDD)."""
    if len(date_part) not in [7, 8]:
        raise ValueError("Invalid ordinal date format")
    
    year = int(date_part[:4])
    day_of_year = int(date_part[4:])
    
    max_days = 366 if _is_leap_year(year) else 365
    if day_of_year < 1 or day_of_year > max_days:
        raise ValueError(f"Day of year must be between 1 and {max_days} for year {year}")
    
    # Convert day of year to month and day
    return _day_of_year_to_date(year, day_of_year)


def _parse_calendar_date(date_part: str) -> tuple[int, int, int]:
    """Parse regular calendar date format."""
    if '-' in date_part:
        parts = date_part.split('-')
        if len(parts) != 3:
            raise ValueError("Invalid date format")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
    else:
        if len(date_part) != 8:
            raise ValueError("Invalid date format")
        year = int(date_part[:4])
        month = int(date_part[4:6])
        day = int(date_part[6:8])
    
    _validate_month(month)
    _validate_day(year, month, day)
    
    return year, month, day


def _parse_time_part(time_part: str) -> tuple[int, int, int, int]:
    """Parse the time part of the ISO string."""
    if not time_part:
        return 0, 0, 0, 0
    
    # Check if it's compact format (no separators)
    if ':' not in time_part and '.' not in time_part and ',' not in time_part:
        return _parse_compact_time(time_part)
    
    # Handle fractional hours/minutes/seconds by splitting on colons only
    # We need to preserve decimal points within components
    parts = time_part.split(':')
    
    if not parts:
        return 0, 0, 0, 0
    
    # Parse hours
    hour_str = parts[0]
    if '.' in hour_str or ',' in hour_str:
        # Fractional hours
        hour_float = float(hour_str.replace(',', '.'))
        hour = int(hour_float)
        minute_fraction = (hour_float - hour) * 60
        minute = int(minute_fraction)
        second_fraction = (minute_fraction - minute) * 60
        second = int(second_fraction)
        microsecond = int((second_fraction - second) * 1000000)
    else:
        hour = int(hour_str)
        minute = 0
        second = 0
        microsecond = 0
        
        if len(parts) > 1:
            # Parse minutes
            minute_str = parts[1]
            if '.' in minute_str or ',' in minute_str:
                # Fractional minutes
                minute_float = float(minute_str.replace(',', '.'))
                minute = int(minute_float)
                second_fraction = (minute_float - minute) * 60
                second = int(second_fraction)
                microsecond = int((second_fraction - second) * 1000000)
            else:
                minute = int(minute_str)
                
                if len(parts) > 2:
                    # Parse seconds
                    second_str = parts[2]
                    if '.' in second_str or ',' in second_str:
                        # Fractional seconds
                        second_float = float(second_str.replace(',', '.'))
                        second = int(second_float)
                        microsecond = int((second_float - second) * 1000000)
                    else:
                        second = int(second_str)
    
    # Validate time components
    if hour < 0 or hour > 24:
        raise ValueError(f"Hour must be between 0 and 24, got {hour}")
    if hour == 24 and (minute != 0 or second != 0 or microsecond != 0):
        raise ValueError("When hour is 24, minutes and seconds must be 0")
    if minute < 0 or minute > 59:
        raise ValueError(f"Minute must be between 0 and 59, got {minute}")
    if second < 0 or second > 59:
        raise ValueError(f"Second must be between 0 and 59, got {second}")
    
    return hour, minute, second, microsecond


def _parse_compact_time(time_part: str) -> tuple[int, int, int, int]:
    """Parse compact time format (HHMMSS or HHMM or HH)."""
    if len(time_part) == 2:
        # HH
        hour = int(time_part)
        return hour, 0, 0, 0
    elif len(time_part) == 4:
        # HHMM
        hour = int(time_part[:2])
        minute = int(time_part[2:4])
        return hour, minute, 0, 0
    elif len(time_part) == 6:
        # HHMMSS
        hour = int(time_part[:2])
        minute = int(time_part[2:4])
        second = int(time_part[4:6])
        return hour, minute, second, 0
    else:
        raise ValueError(f"Invalid compact time format: {time_part}")


def _parse_timezone_part(timezone_part: str) -> timezone:
    """Parse the timezone part of the ISO string."""
    if timezone_part == 'Z':
        return timezone.utc
    
    # Parse offset format (+/-HH:MM or +/-HHMM or +/-HH)
    match = re.match(r'^([+-])(\d{2})(?::?(\d{2}))?$', timezone_part)
    if not match:
        raise ValueError(f"Invalid timezone format: {timezone_part}")
    
    sign_str, hours_str, minutes_str = match.groups()
    sign = 1 if sign_str == '+' else -1
    hours = int(hours_str)
    minutes = int(minutes_str) if minutes_str else 0
    
    if hours > 23:
        raise ValueError(f"Timezone hour offset cannot exceed 23, got {hours}")
    if minutes > 59:
        raise ValueError(f"Timezone minute offset cannot exceed 59, got {minutes}")
    
    total_minutes = sign * (hours * 60 + minutes)
    return timezone(timedelta(minutes=total_minutes))


def _iso_week_to_date(year: int, week: int, weekday: int) -> tuple[int, int, int]:
    """Convert ISO week date to calendar date."""
    # January 4th is always in week 1
    jan4 = datetime(year, 1, 4)
    
    # Find Monday of week 1
    days_from_monday = jan4.weekday()
    monday_week1 = jan4 - timedelta(days=days_from_monday)
    
    # Calculate the target date
    target_date = monday_week1 + timedelta(weeks=week - 1, days=weekday - 1)
    
    return target_date.year, target_date.month, target_date.day


def _day_of_year_to_date(year: int, day_of_year: int) -> tuple[int, int, int]:
    """Convert day of year to month and day."""
    temp_date = datetime(year, 1, 1) + timedelta(days=day_of_year - 1)
    return temp_date.year, temp_date.month, temp_date.day


def _is_leap_year(year: int) -> bool:
    """Check if a year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def _validate_month(month: int) -> None:
    """Validate month value."""
    if month < 1 or month > 12:
        raise ValueError(f"Month must be between 1 and 12, got {month}")


def _validate_day(year: int, month: int, day: int) -> None:
    """Validate day value for given year and month."""
    if day < 1:
        raise ValueError(f"Day must be at least 1, got {day}")
    
    # Days in each month
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Adjust for leap year
    if _is_leap_year(year):
        days_in_month[1] = 29
    
    max_day = days_in_month[month - 1]
    if day > max_day:
        raise ValueError(f"Day {day} is invalid for month {month} in year {year}")
