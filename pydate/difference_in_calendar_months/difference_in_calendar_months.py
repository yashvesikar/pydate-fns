from datetime import datetime
from typing import Union

from ..to_date import to_date


def difference_in_calendar_months(later_date: Union[datetime, float, int], earlier_date: Union[datetime, float, int]) -> float:
    """
    Get the number of calendar months between the given dates.

    :param later_date: The later date
    :param earlier_date: The earlier date
    :return: The number of calendar months between the dates. Returns NaN if either date is invalid.

    Example:
        >>> # How many calendar months are between 31 January 2014 and 1 September 2014?
        >>> result = difference_in_calendar_months(
        >>>     datetime(2014, 9, 1),    # Sep 1 2014
        >>>     datetime(2014, 1, 31)    # Jan 31 2014
        >>> )
        >>> # => 8
    """
    try:
        later = to_date(later_date)
        earlier = to_date(earlier_date)
    except (TypeError, ValueError):
        return float('nan')

    years_diff = later.year - earlier.year
    months_diff = later.month - earlier.month

    return years_diff * 12 + months_diff