from datetime import datetime
from typing import Union
import math
from ..to_date import to_date
from ..sub_days import sub_days


def previous_day(date: Union[datetime, int, float], day: Union[int, float]) -> datetime:
    """
    When is the previous day of the week?
    
    When is the previous day of the week? 0-6 the day of the week, 0 represents Sunday.
    
    Args:
        date: The date to check
        day: Day of the week (0=Sunday, 1=Monday, 2=Tuesday, ..., 6=Saturday)
        
    Returns:
        The date is the previous day of week
        
    Examples:
        >>> from datetime import datetime
        >>> # When is the previous Monday before Mar, 20, 2020?
        >>> previous_day(datetime(2020, 3, 20), 1)
        datetime.datetime(2020, 3, 16, 0, 0)
        >>> # When is the previous Tuesday before Mar, 21, 2020?
        >>> previous_day(datetime(2020, 3, 21), 2)
        datetime.datetime(2020, 3, 17, 0, 0)
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
    
    day_int = int(day)
    
    # Convert Python weekday to JavaScript weekday (0=Sunday, 6=Saturday)
    current_day_js = (dt.weekday() + 1) % 7
    
    # Calculate delta to previous occurrence of the target day
    delta = current_day_js - day_int
    if delta <= 0:
        delta += 7
    
    return sub_days(dt, delta)