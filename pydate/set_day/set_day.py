from datetime import datetime, timedelta
from typing import Union, Optional
import math
from ..to_date import to_date


def set_day(date: Union[datetime, int, float], day: Union[int, float], week_starts_on: Optional[int] = None) -> datetime:
    """
    Set the day of the week to the given date.
    
    Set the day of the week to the given date.
    
    Args:
        date: The date to be changed
        day: The day of the week of the new date (0=Sunday, 1=Monday, etc.)
        week_starts_on: Which day of the week is the first day of the week (0=Sunday, 1=Monday, etc.)
        
    Returns:
        The new date with the day of the week set
        
    Examples:
        >>> from datetime import datetime
        >>> # Set week day to Sunday, with the default weekStartsOn of Sunday:
        >>> set_day(datetime(2014, 9, 1), 0)  # Sep 1, 2014 was Monday, setting to Sunday
        datetime.datetime(2014, 8, 31, 0, 0)
        >>> # Set week day to Sunday, with a weekStartsOn of Monday:
        >>> set_day(datetime(2014, 9, 1), 0, week_starts_on=1)
        datetime.datetime(2014, 9, 7, 0, 0)
    """
    # Handle NaN day
    if isinstance(day, float) and math.isnan(day):
        class InvalidDateTime(datetime):
            def timestamp(self):
                return float('nan')
        return InvalidDateTime(1970, 1, 1)
    
    dt = to_date(date)
    
    # Handle NaN input date
    try:
        if math.isnan(dt.timestamp()):
            return dt
    except (ValueError, OSError):
        return dt
    
    # Default week starts on Sunday (0)
    if week_starts_on is None:
        week_starts_on = 0
    
    day_int = int(day)
    current_day = dt.weekday()  # Python weekday: 0=Monday, 6=Sunday
    
    # Convert Python weekday to JavaScript weekday (0=Sunday, 6=Saturday)
    current_day_js = (current_day + 1) % 7
    
    # Handle day overflow/underflow like JavaScript
    remainder = day_int % 7
    day_index = (remainder + 7) % 7
    
    # Calculate the difference accounting for week start
    delta = 7 - week_starts_on
    
    if day_int < 0 or day_int > 6:
        # Handle overflow/underflow days
        diff = day_int - ((current_day_js + delta) % 7)
    else:
        # Normal case
        diff = ((day_index + delta) % 7) - ((current_day_js + delta) % 7)
    
    return dt + timedelta(days=diff)