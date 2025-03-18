from datetime import datetime
from typing import Union

from ..to_date import to_date


def get_seconds(date: Union[datetime, float, int]) -> int:
    """
    Get the seconds of the given date.

    :param date: The given date
    :return: The seconds (0-59)

    Example:
        >>> # Get the seconds of 29 February 2012 11:45:05.123:
        >>> result = get_seconds(datetime(2012, 2, 29, 11, 45, 5, 123000))
        >>> # => 5
    """
    try:
        dt = to_date(date)
        return dt.second
    except (TypeError, ValueError):
        return float('nan')