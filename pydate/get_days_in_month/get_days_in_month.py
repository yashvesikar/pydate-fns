
import calendar
from datetime import datetime
from typing import Union

from ..to_date.to_date import to_date


def get_days_in_month(date: Union[datetime, int, float]) -> int:
    """
    Get the number of days in a month of the given date.

    :param date: The given date
    :return int: The number of days in a month
    
    Examples:
        >>> from datetime import datetime
        >>> # How many days are in February 2000?
        >>> result = get_days_in_month(datetime(2000, 2, 1))
        >>> result
        29
        
        >>> # How many days are in February 2001 (non-leap year)?
        >>> result = get_days_in_month(datetime(2001, 2, 1))
        >>> result
        28
        
        >>> # Accepts timestamps
        >>> result = get_days_in_month(datetime(2000, 2, 1).timestamp())
        >>> result
        29
    """
    _date = to_date(date)
    # Use Python's calendar module which handles leap years automatically
    return calendar.monthrange(_date.year, _date.month)[1]
