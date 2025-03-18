from datetime import datetime
from typing import Union

from ..to_date import to_date


def get_month(date: Union[datetime, float, int]) -> int:
    """
    Get the month of the given date.

    :param date: The given date
    :return: The month (1-12)

    Example:
        >>> # Which month is 29 February 2012?
        >>> result = get_month(datetime(2012, 2, 29))
        >>> # => 2
    """
    try:
        dt = to_date(date)
        return dt.month  # Keep Python's 1-12 month range
    except (TypeError, ValueError):
        return float('nan')