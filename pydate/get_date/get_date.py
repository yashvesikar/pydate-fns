from datetime import datetime
from typing import Union

from ..to_date import to_date


def get_date(date: Union[datetime, float, int]) -> int:
    """
    Get the day of the month of the given date.

    :param date: The given date
    :return: The day of month (1-31)

    Example:
        >>> # Which day of the month is 29 February 2012?
        >>> result = get_date(datetime(2012, 2, 29))
        >>> # => 29
    """
    try:
        dt = to_date(date)
        return dt.day
    except (TypeError, ValueError):
        return float('nan')