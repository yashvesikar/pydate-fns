from datetime import datetime
import math
from typing import Union
from ..compare_asc import compare_asc
from ..difference_in_calendar_years import difference_in_calendar_years
from ..to_date import to_date

def difference_in_years(
    later_date: Union[datetime, float, int],
    earlier_date: Union[datetime, float, int]
) -> Union[int, float]:
    """Get the number of full years between the given dates.

    Args:
        later_date: The later date
        earlier_date: The earlier date

    Returns:
        The number of full years.
        Returns NaN if either date is invalid.

    Example:
        >>> from datetime import datetime
        >>> date1 = datetime(2015, 2, 11)
        >>> date2 = datetime(2013, 12, 31)
        >>> difference_in_years(date1, date2)
        1
    """
    try:
        later_date = to_date(later_date)
        earlier_date = to_date(earlier_date)
    except (TypeError, ValueError):
        return float('nan')

    # -1 if the left date is earlier than the right date
    sign = compare_asc(later_date, earlier_date)

    # First calculate the difference in calendar years
    difference = abs(difference_in_calendar_years(later_date, earlier_date))

    # Create copies to avoid modifying the original dates
    later_date_copy = datetime(
        1584,  # Use same arbitrary year as JavaScript implementation
        later_date.month,
        later_date.day,
        later_date.hour,
        later_date.minute,
        later_date.second,
        later_date.microsecond
    )
    earlier_date_copy = datetime(
        1584,  # Use same arbitrary year as JavaScript implementation
        earlier_date.month,
        earlier_date.day,
        earlier_date.hour,
        earlier_date.minute,
        earlier_date.second,
        earlier_date.microsecond
    )

    # For it to be true, when the later date is indeed later than the earlier date
    # (2026-02-01 - 2023-12-10 = 3 years), the difference is full if
    # the normalized later date is also later than the normalized earlier date.
    # In our example, 1584-02-01 is earlier than 1584-12-10, so the difference
    # is partial, hence we need to subtract 1 from the difference 3 - 1 = 2.
    is_partial = compare_asc(later_date_copy, earlier_date_copy) == -sign

    result = sign * (difference - int(is_partial))

    # Prevent negative zero
    return 0 if result == 0 else result