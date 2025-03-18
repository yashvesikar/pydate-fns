from datetime import datetime
from typing import Union

from ..to_date import to_date


def get_year(date: Union[datetime, float, int]) -> int:
    """
    Get the year of the given date.

    :param date: The given date
    :return: The year

    Example:
        >>> # Which year is 2 July 2014?
        >>> result = get_year(datetime(2014, 7, 2))
        >>> # => 2014
    """
    try:
        dt = to_date(date)
        return dt.year
    except (TypeError, ValueError):
        return float('nan')