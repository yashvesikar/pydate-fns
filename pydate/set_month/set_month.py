
from datetime import datetime, timedelta
from typing import Union
import math
from ..to_date import to_date


def set_month(date: Union[datetime, int, float], month: Union[int, float]) -> datetime:
    """
    Set the month to the given date.
    
    Set the month to the given date. This function mimics JavaScript's Date.setMonth()
    behavior but uses Python's 1-indexed months (1=January, 12=December).
    Like JavaScript, days that don't exist in the target month will overflow to
    subsequent months rather than being clamped.
    
    Args:
        date: The date to be changed
        month: The month to set (1-12, where 1=January, 12=December)
               Values outside 1-12 will adjust the year accordingly
        
    Returns:
        The new date with the month set
        
    Examples:
        >>> from datetime import datetime
        >>> # Set February to 1 September 2014:
        >>> set_month(datetime(2014, 9, 1), 2)
        datetime.datetime(2014, 2, 1, 0, 0)
        >>> # January 31 becomes March 3rd in non-leap year (day overflow):
        >>> set_month(datetime(2014, 1, 31), 2)
        datetime.datetime(2014, 3, 3, 0, 0)
        >>> # January 31 becomes March 2nd in leap year (day overflow):
        >>> set_month(datetime(2016, 1, 31), 2)
        datetime.datetime(2016, 3, 2, 0, 0)
        >>> # Month 0 becomes December of previous year:
        >>> set_month(datetime(2014, 6, 15), 0)
        datetime.datetime(2013, 12, 15, 0, 0)
    """
    # Handle NaN month
    if isinstance(month, float) and math.isnan(month):
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
    
    month_int = int(month)
    
    # Convert Python month (1-12) to JavaScript equivalent (0-11) for calculation
    js_month = month_int - 1
    
    # Calculate year offset and final month using JavaScript logic
    year_offset = js_month // 12
    final_month = (js_month % 12) + 1
    final_year = dt.year + year_offset
    
    # Get the current day for overflow calculation
    current_day = dt.day
    
    # Create target date with day 1, then add (original_day - 1) days
    # This naturally handles day overflow like JavaScript
    target_date = dt.replace(year=final_year, month=final_month, day=1)
    result_date = target_date + timedelta(days=current_day - 1)
    
    return result_date
