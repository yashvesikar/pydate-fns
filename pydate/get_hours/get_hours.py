from datetime import datetime
from typing import Union

from ..to_date import to_date


def get_hours(date: Union[datetime, float, int]) -> int:
    """
    Get the hours of the given date.

    :param date: The given date
    :return: The hours (0-23)

    Example:
        >>> # Get the hours of 29 February 2012 11:45:00:
        >>> result = get_hours(datetime(2012, 2, 29, 11, 45))
        >>> # => 11
    """
    try:
        dt = to_date(date)
        return dt.hour
    except (TypeError, ValueError):
        return float('nan')