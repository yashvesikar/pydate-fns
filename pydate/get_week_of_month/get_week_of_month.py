from datetime import datetime
from typing import Union, Optional
import math
from ..to_date import to_date
from ..get_date import get_date
from ..start_of_month import start_of_month


def get_week_of_month(date: Union[datetime, int, float], week_starts_on: Optional[int] = None) -> Union[int, float]:
    """
    Get the week of the month of the given date.
    
    Get the week of the month of the given date.
    
    Args:
        date: The given date
        week_starts_on: Which day of the week is the first day of the week (0=Sunday, 1=Monday, etc.)
        
    Returns:
        The week of month
        
    Examples:
        >>> from datetime import datetime
        >>> # Which week of the month is 9 November 2017?
        >>> get_week_of_month(datetime(2017, 11, 9))
        2
    """
    try:
        dt = to_date(date)
        
        # Handle NaN input date
        if math.isnan(dt.timestamp()):
            return float('nan')
            
        # Default week starts on Sunday (0)
        if week_starts_on is None:
            week_starts_on = 0
            
        current_day_of_month = get_date(dt)
        if math.isnan(current_day_of_month):
            return float('nan')
        
        # Get the start of the month
        month_start = start_of_month(dt)
        
        # Convert Python weekday to JavaScript weekday (0=Sunday, 6=Saturday)
        start_week_day = (month_start.weekday() + 1) % 7
        
        # Calculate the last day of the first week
        last_day_of_first_week = week_starts_on - start_week_day
        if last_day_of_first_week <= 0:
            last_day_of_first_week += 7
        
        # Calculate remaining days after first week
        remaining_days_after_first_week = current_day_of_month - last_day_of_first_week
        
        return math.ceil(remaining_days_after_first_week / 7) + 1
        
    except (ValueError, TypeError, OSError):
        return float('nan')