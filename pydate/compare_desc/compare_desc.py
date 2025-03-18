from datetime import datetime
from typing import Union

from ..to_date import to_date


def compare_desc(date_left: Union[datetime, float, int], date_right: Union[datetime, float, int]) -> float:
    """
    Compare the two dates reverse chronologically and return -1, 0 or 1.

    Compare the two dates and return -1 if the first date is after the second,
    1 if the first date is before the second or 0 if dates are equal.

    :param date_left: The first date to compare
    :param date_right: The second date to compare
    :return: The result of the comparison (-1, 0, 1, or NaN)

    Example:
        >>> # Compare 11 February 1987 and 10 July 1989 reverse chronologically:
        >>> result = compare_desc(datetime(1987, 2, 11), datetime(1989, 7, 10))
        >>> # => 1

        >>> # Sort the array of dates in reverse chronological order:
        >>> result = sorted([
        >>>     datetime(1995, 7, 2),
        >>>     datetime(1987, 2, 11),
        >>>     datetime(1989, 7, 10)
        >>> ], key=lambda x: x.timestamp(), reverse=True)
        >>> # => [
        >>> #   datetime(1995, 7, 2),
        >>> #   datetime(1989, 7, 10),
        >>> #   datetime(1987, 2, 11)
        >>> # ]
    """
    try:
        left = to_date(date_left)
        right = to_date(date_right)
        diff = (left.timestamp() - right.timestamp()) * 1000  # Convert to milliseconds like JS
    except (TypeError, ValueError):
        return float('nan')

    if diff > 0:
        return -1
    elif diff < 0:
        return 1
    return 0  # Always return 0 for equal dates, not diff