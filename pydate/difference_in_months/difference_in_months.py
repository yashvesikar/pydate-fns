from datetime import datetime, timedelta
import math
from typing import Union
from ..compare_asc import compare_asc
from ..difference_in_calendar_months import difference_in_calendar_months
from ..is_last_day_of_month import is_last_day_of_month
from ..to_date import to_date

def difference_in_months(
    later_date: Union[datetime, float, int],
    earlier_date: Union[datetime, float, int]
) -> Union[int, float]:
    """Get the number of full months between the given dates.

    Args:
        later_date: The later date
        earlier_date: The earlier date

    Returns:
        The number of full months.
        Returns NaN if either date is invalid.

    Example:
        >>> from datetime import datetime
        >>> date1 = datetime(2014, 9, 1)
        >>> date2 = datetime(2014, 1, 31)
        >>> difference_in_months(date1, date2)
        7
    """
    try:
        later_date = to_date(later_date)
        earlier_date = to_date(earlier_date)
    except (TypeError, ValueError):
        return float('nan')

    # Create a working copy of later_date that we can modify
    working_later_date = datetime(
        later_date.year,
        later_date.month,
        later_date.day,
        later_date.hour,
        later_date.minute,
        later_date.second,
        later_date.microsecond
    )

    sign = compare_asc(working_later_date, earlier_date)
    difference = abs(difference_in_calendar_months(working_later_date, earlier_date))

    if difference < 1:
        return 0

    # Handle special case for February
    if working_later_date.month == 2 and working_later_date.day > 27:
        # For February, use the last day of the month
        if working_later_date.month == 12:
            next_year = working_later_date.year + 1
            next_month = 1
        else:
            next_year = working_later_date.year
            next_month = working_later_date.month + 1
        working_later_date = datetime(
            next_year,
            next_month,
            1,
            working_later_date.hour,
            working_later_date.minute,
            working_later_date.second,
            working_later_date.microsecond
        ) - timedelta(days=1)

    # Adjust the month by the difference
    year_diff = (working_later_date.month - sign * difference) // 12
    new_month = (working_later_date.month - sign * difference) % 12 or 12
    new_year = working_later_date.year - year_diff
    
    # Create new date with adjusted month
    try:
        working_later_date = datetime(
            new_year,
            new_month,
            working_later_date.day,
            working_later_date.hour,
            working_later_date.minute,
            working_later_date.second,
            working_later_date.microsecond
        )
    except ValueError:
        # If the day doesn't exist in the target month (e.g., March 31 -> February 31),
        # use the last day of the target month
        if working_later_date.day > 28:
            working_later_date = datetime(
                new_year,
                new_month,
                1,  # Start with first day of month
                working_later_date.hour,
                working_later_date.minute,
                working_later_date.second,
                working_later_date.microsecond
            )
            # Move to last day of month
            if new_month == 12:
                next_year = new_year + 1
                next_month = 1
            else:
                next_year = new_year
                next_month = new_month + 1
            working_later_date = datetime(
                next_year,
                next_month,
                1,
                working_later_date.hour,
                working_later_date.minute,
                working_later_date.second,
                working_later_date.microsecond
            )
            working_later_date = working_later_date.replace(day=1) - timedelta(days=1)

    is_last_month_not_full = compare_asc(working_later_date, earlier_date) == -sign

    # Special case: if later_date is last day of month and difference is 1 month
    if (
        is_last_day_of_month(later_date) and
        difference == 1 and
        compare_asc(later_date, earlier_date) == 1
    ):
        is_last_month_not_full = False

    result = sign * (difference - int(is_last_month_not_full))

    # Prevent negative zero
    return 0 if result == 0 else result