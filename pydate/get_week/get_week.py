
from datetime import datetime
from typing import Union, Optional
import math
from ..to_date import to_date
from ..start_of_week import start_of_week


def get_week_year(date: Union[datetime, int, float], week_starts_on: Optional[int] = None, first_week_contains_date: Optional[int] = None) -> int:
    """
    Get the local week-numbering year of the given date.
    """
    dt = to_date(date)
    year = dt.year
    
    if week_starts_on is None:
        week_starts_on = 0
    if first_week_contains_date is None:
        first_week_contains_date = 1
    
    # Create first week of next year
    first_week_of_next_year = datetime(year + 1, 1, first_week_contains_date)
    start_of_next_year = start_of_week(first_week_of_next_year, week_starts_on)
    
    # Create first week of this year
    first_week_of_this_year = datetime(year, 1, first_week_contains_date)
    start_of_this_year = start_of_week(first_week_of_this_year, week_starts_on)
    
    if dt >= start_of_next_year:
        return year + 1
    elif dt >= start_of_this_year:
        return year
    else:
        return year - 1


def start_of_week_year(date: Union[datetime, int, float], week_starts_on: Optional[int] = None, first_week_contains_date: Optional[int] = None) -> datetime:
    """
    Return the start of a local week-numbering year for the given date.
    """
    if week_starts_on is None:
        week_starts_on = 0
    if first_week_contains_date is None:
        first_week_contains_date = 1
    
    year = get_week_year(date, week_starts_on, first_week_contains_date)
    first_week = datetime(year, 1, first_week_contains_date)
    return start_of_week(first_week, week_starts_on)


def get_week(date: Union[datetime, int, float], week_starts_on: Optional[int] = None, first_week_contains_date: Optional[int] = None) -> int:
    """
    Get the local week index of the given date.
    
    Get the local week index of the given date.
    The exact calculation depends on the values of
    `week_starts_on` (which is the index of the first day of the week)
    and `first_week_contains_date` (which is the day of January, which is always in
    the first week of the week-numbering year)
    
    Args:
        date: The given date
        week_starts_on: Which day of the week is the first day of the week (0=Sunday, 1=Monday, etc.)
        first_week_contains_date: Which day of January is always in the first week (default: 1)
        
    Returns:
        The week number
        
    Examples:
        >>> from datetime import datetime
        >>> # Which week of the local week numbering year is 2 January 2005 with default options?
        >>> get_week(datetime(2005, 1, 2))
        2
    """
    try:
        dt = to_date(date)
        
        # Check for invalid date (NaN)
        if math.isnan(dt.timestamp()):
            return float('nan')
            
        if week_starts_on is None:
            week_starts_on = 0
        if first_week_contains_date is None:
            first_week_contains_date = 1
        
        # Calculate difference between start of current week and start of week year
        current_week_start = start_of_week(dt, week_starts_on)
        week_year_start = start_of_week_year(dt, week_starts_on, first_week_contains_date)
        
        # Calculate milliseconds in a week (7 * 24 * 60 * 60 * 1000)
        milliseconds_in_week = 7 * 24 * 60 * 60 * 1000
        
        # Get difference in milliseconds
        diff_ms = (current_week_start.timestamp() - week_year_start.timestamp()) * 1000
        
        # Round to nearest integer to handle DST issues and add 1 for 1-indexed weeks
        return round(diff_ms / milliseconds_in_week) + 1
        
    except (ValueError, OSError, OverflowError):
        return float('nan')
