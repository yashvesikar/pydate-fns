from datetime import datetime
from typing import Union
import math
from ..to_date import to_date
from ..add_days import add_days


def next_day(date: Union[datetime, int, float], day: Union[int, float]) -> datetime:
    """
    When is the next day of the week?
    
    When is the next day of the week? 0-6 the day of the week, 0 represents Sunday.
    
    Args:
        date: The date to check
        day: Day of the week (0=Sunday, 1=Monday, 2=Tuesday, ..., 6=Saturday)
        
    Returns:
        The date is the next day of the week
        
    Examples:
        >>> from datetime import datetime
        >>> # When is the next Monday after Mar, 20, 2020?
        >>> next_day(datetime(2020, 3, 20), 1)
        datetime.datetime(2020, 3, 23, 0, 0)
        >>> # When is the next Tuesday after Mar, 21, 2020?
        >>> next_day(datetime(2020, 3, 21), 2)
        datetime.datetime(2020, 3, 24, 0, 0)
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
    
    # Calculate delta to next occurrence of the target day
    delta = day_int - current_day_js
    if delta <= 0:
        delta += 7
    
    return add_days(dt, delta)