from datetime import datetime, timedelta
import math
from typing import Union
from ..difference_in_calendar_days import difference_in_calendar_days
from ..to_date import to_date

def compare_local_asc(later_date: datetime, earlier_date: datetime) -> int:
    """Compare two dates in local time, similar to compareAsc but using local time not UTC."""
    diff = (
        later_date.year - earlier_date.year or
        later_date.month - earlier_date.month or
        later_date.day - earlier_date.day or
        later_date.hour - earlier_date.hour or
        later_date.minute - earlier_date.minute or
        later_date.second - earlier_date.second or
        later_date.microsecond // 1000 - earlier_date.microsecond // 1000
    )

    if diff < 0:
        return -1
    if diff > 0:
        return 1
    return diff  # Return 0 if diff is 0; return NaN if diff is NaN

def difference_in_days(
    later_date: Union[datetime, float, int],
    earlier_date: Union[datetime, float, int]
) -> Union[int, float]:
    """Get the number of full days between the given dates.

    One "full day" is the distance between a local time in one day to the same
    local time on the next or previous day. A full day can sometimes be less than
    or more than 24 hours if a daylight savings change happens between two dates.

    To ignore DST and only measure exact 24-hour periods, use this instead:
    `int(difference_in_hours(later_date, earlier_date) / 24)`

    Args:
        later_date: The later date
        earlier_date: The earlier date

    Returns:
        The number of full days according to the local timezone.
        Returns NaN if either date is invalid.

    Example:
        >>> from datetime import datetime
        >>> date1 = datetime(2012, 7, 2, 0, 0)
        >>> date2 = datetime(2011, 7, 2, 23, 0)
        >>> difference_in_days(date1, date2)
        365
    """
    try:
        later_date = to_date(later_date)
        earlier_date = to_date(earlier_date)
    except (TypeError, ValueError):
        return float('nan')

    sign = compare_local_asc(later_date, earlier_date)
    difference = abs(difference_in_calendar_days(later_date, earlier_date))

    # Create a new date to avoid modifying the original and adjust by the difference in days
    later_date_copy = later_date - timedelta(days=sign * difference)

    # Math.abs(diff in full days - diff in calendar days) === 1 if last calendar day is not full
    # If so, result must be decreased by 1 in absolute value
    is_last_day_not_full = int(compare_local_asc(later_date_copy, earlier_date) == -sign)
    result = sign * (difference - is_last_day_not_full)

    # Prevent negative zero
    return 0 if result == 0 else result