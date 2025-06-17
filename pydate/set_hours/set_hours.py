
from datetime import datetime, timedelta
from typing import Union
import math
from ..to_date import to_date


def set_hours(date: Union[datetime, int, float], hours: Union[int, float]) -> datetime:
    """
    Set the hours to the given date.
    
    Set the hours to the given date. Hours overflow will adjust the date accordingly.
    
    Args:
        date: The date to be changed
        hours: The hours of the new date (0-23, but overflow is allowed)
        
    Returns:
        The new date with the hours set
        
    Examples:
        >>> from datetime import datetime
        >>> # Set 4 hours to 1 September 2014 11:30:00:
        >>> set_hours(datetime(2014, 9, 1, 11, 30), 4)
        datetime.datetime(2014, 9, 1, 4, 30)
        >>> # Hour 25 overflows to next day:
        >>> set_hours(datetime(2014, 9, 1, 11, 30), 25)
        datetime.datetime(2014, 9, 2, 1, 30)
    """
    # Handle NaN hours
    if isinstance(hours, float) and math.isnan(hours):
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
    
    # Reset to start of day, then add hours (handles overflow like JavaScript)
    start_of_day = dt.replace(hour=0)
    return start_of_day + timedelta(hours=int(hours))
