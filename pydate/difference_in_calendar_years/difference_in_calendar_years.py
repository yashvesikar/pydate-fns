from datetime import datetime
import math
from typing import Union
from ..to_date import to_date

def difference_in_calendar_years(
    later_date: Union[datetime, float, int],
    earlier_date: Union[datetime, float, int]
) -> Union[int, float]:
    """Get the number of calendar years between the given dates.

    Args:
        later_date: The later date
        earlier_date: The earlier date

    Returns:
        The number of calendar years.
        Returns NaN if either date is invalid.

    Example:
        >>> from datetime import datetime
        >>> date1 = datetime(2015, 2, 11)
        >>> date2 = datetime(2013, 12, 31)
        >>> difference_in_calendar_years(date1, date2)
        2
    """
    try:
        later_date = to_date(later_date)
        earlier_date = to_date(earlier_date)
    except (TypeError, ValueError):
        return float('nan')

    result = later_date.year - earlier_date.year

    # Prevent negative zero
    return 0 if result == 0 else result