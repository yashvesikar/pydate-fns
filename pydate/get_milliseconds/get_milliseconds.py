from datetime import datetime
from typing import Union

from ..to_date import to_date


def get_milliseconds(date: Union[datetime, float, int]) -> int:
    """
    Get the milliseconds of the given date.

    :param date: The given date
    :return: The milliseconds (0-999)

    Example:
        >>> # Get the milliseconds of 29 February 2012 11:45:05.123:
        >>> result = get_milliseconds(datetime(2012, 2, 29, 11, 45, 5, 123000))
        >>> # => 123
    """
    try:
        dt = to_date(date)
        return dt.microsecond // 1000  # Convert microseconds to milliseconds
    except (TypeError, ValueError):
        return float('nan')