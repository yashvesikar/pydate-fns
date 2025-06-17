
import calendar
from datetime import datetime
from typing import Union

from ..to_date.to_date import to_date


def get_days_in_year(date: Union[datetime, int, float]) -> int:
    """
    Get the number of days in a year of the given date.

    :param date: The given date
    :return int: The number of days in a year (365 or 366)
    
    Examples:
        >>> from datetime import datetime
        >>> # How many days are in 2012?
        >>> result = get_days_in_year(datetime(2012, 1, 1))
        >>> result
        366
        
        >>> # How many days are in 2013 (non-leap year)?
        >>> result = get_days_in_year(datetime(2013, 1, 1))
        >>> result
        365
        
        >>> # Accepts timestamps
        >>> result = get_days_in_year(datetime(2012, 1, 1).timestamp())
        >>> result
        366
    """
    _date = to_date(date)
    # Use calendar.isleap to determine if it's a leap year
    return 366 if calendar.isleap(_date.year) else 365
