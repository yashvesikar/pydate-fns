
from datetime import datetime
from typing import Union
import math
from ..to_date import to_date


def set_year(date: Union[datetime, int, float], year: Union[int, float]) -> datetime:
    """
    Set the year to the given date.
    
    Set the year to the given date. Note that February 29 in non-leap years
    will be adjusted to February 28.
    
    Args:
        date: The date to be changed
        year: The year of the new date
        
    Returns:
        The new date with the year set
        
    Examples:
        >>> from datetime import datetime
        >>> # Set year 2013 to 1 September 2014:
        >>> set_year(datetime(2014, 9, 1), 2013)
        datetime.datetime(2013, 9, 1, 0, 0)
        >>> # February 29 becomes February 28 in non-leap year:
        >>> set_year(datetime(2016, 2, 29), 2015)
        datetime.datetime(2015, 2, 28, 0, 0)
    """
    # Handle NaN year
    if isinstance(year, float) and math.isnan(year):
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
    
    year_int = int(year)
    
    # Handle February 29 in leap year → non-leap year
    if dt.month == 2 and dt.day == 29:
        # Check if target year is a leap year
        if not ((year_int % 4 == 0 and year_int % 100 != 0) or (year_int % 400 == 0)):
            # Target year is not a leap year, adjust to Feb 28
            return dt.replace(year=year_int, day=28)
    
    return dt.replace(year=year_int)
