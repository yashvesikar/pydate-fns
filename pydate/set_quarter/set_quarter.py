
from datetime import datetime, timedelta
from typing import Union
import math
from ..to_date import to_date
from ..get_quarter import get_quarter


def set_quarter(date: Union[datetime, int, float], quarter: Union[int, float]) -> datetime:
    """
    Set the year quarter to the given date.
    
    Set the year quarter to the given date.
    
    Args:
        date: The date to be changed
        quarter: The quarter of the new date (1-4)
        
    Returns:
        The new date with the quarter set
        
    Examples:
        >>> from datetime import datetime
        >>> # Set the 2nd quarter to 2 July 2014:
        >>> set_quarter(datetime(2014, 7, 2), 2)
        datetime.datetime(2014, 4, 2, 0, 0)
    """
    dt = to_date(date)
    
    # Handle NaN quarter
    if isinstance(quarter, float) and math.isnan(quarter):
        # Return an invalid date
        raise ValueError("Quarter cannot be NaN")
    
    quarter = int(quarter)
    
    # Get the current quarter (1-4)
    old_quarter = get_quarter(dt)
    
    # Calculate the difference in months
    diff = quarter - old_quarter
    month_diff = diff * 3
    
    # Calculate new month
    new_month = dt.month + month_diff
    new_year = dt.year
    
    # Handle month overflow/underflow
    while new_month > 12:
        new_month -= 12
        new_year += 1
    while new_month < 1:
        new_month += 12
        new_year -= 1
    
    # Try to create the new date with the same day
    try:
        return dt.replace(year=new_year, month=new_month)
    except ValueError:
        # Day doesn't exist in the target month (e.g., Jan 31 -> Feb 31)
        # Use the last day of the month
        if new_month == 12:
            next_month_first = datetime(new_year + 1, 1, 1)
        else:
            next_month_first = datetime(new_year, new_month + 1, 1)
        
        last_day = next_month_first - timedelta(days=1)
        return dt.replace(
            year=last_day.year,
            month=last_day.month,
            day=last_day.day
        )
