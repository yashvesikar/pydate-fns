from datetime import datetime, timedelta
from typing import Union

from ..to_date import to_date


def add_minutes(date: Union[datetime, float, int], amount: int) -> datetime:
    """
    Add the specified number of minutes to the given date.

    :param date: The date to be changed
    :param amount: The amount of minutes to be added
    :return: The new date with the minutes added. Returns Invalid Date if the date is invalid or amount is NaN.

    Example:
        >>> # Add 30 minutes to 10 July 2014 12:00:00:
        >>> result = add_minutes(datetime(2014, 7, 10, 12, 0), 30)
        >>> # => datetime(2014, 7, 10, 12, 30)
    """
    try:
        # Convert input to datetime and validate amount
        dt = to_date(date)
        if isinstance(amount, float) and amount != amount:  # NaN check
            return datetime(year=1, month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
        
        # Add minutes using timedelta
        return dt + timedelta(minutes=amount)
    except (TypeError, ValueError):
        # Return "Invalid Date" equivalent in Python (datetime with minimum values)
        return datetime(year=1, month=1, day=1, hour=0, minute=0, second=0, microsecond=0)