from datetime import datetime
from typing import Union

from ..to_date import to_date


def get_minutes(date: Union[datetime, float, int]) -> int:
    """
    Get the minutes of the given date.

    :param date: The given date
    :return: The minutes (0-59)

    Example:
        >>> # Get the minutes of 29 February 2012 11:45:05:
        >>> result = get_minutes(datetime(2012, 2, 29, 11, 45, 5))
        >>> # => 45
    """
    try:
        dt = to_date(date)
        return dt.minute
    except (TypeError, ValueError):
        return float('nan')