
import math
from datetime import datetime
from typing import Union

from ..is_date.is_date import is_date
from ..to_date.to_date import to_date


def is_valid(date: Union[datetime, int, float, str, None]) -> bool:
    """
    Returns false if argument is Invalid Date and true otherwise.
    
    Argument is converted to datetime using to_date. Invalid Date is a datetime
    whose timestamp value is NaN or cannot be converted to a valid datetime.

    :param date: The date to check
    :return bool: True if the date is valid, False otherwise
    
    Examples:
        >>> from datetime import datetime
        >>> is_valid(datetime(2014, 2, 31))  # Valid date
        True
        >>> is_valid(1393804800)  # Valid timestamp
        True
        >>> is_valid(float('nan'))  # Invalid - NaN
        False
        >>> is_valid('invalid')  # Invalid string
        False
        >>> is_valid(None)  # Invalid None
        False
    """
    # Handle None case
    if date is None:
        return False
    
    # Handle string cases that can't be converted
    if isinstance(date, str):
        return False
    
    # Handle NaN for float inputs
    if isinstance(date, float) and math.isnan(date):
        return False
    
    # Try to convert to datetime and check if it's valid
    try:
        converted_date = to_date(date)
        # Check if the converted datetime is valid (not None and has valid timestamp)
        if converted_date is None:
            return False
        # Additional check: ensure the timestamp is not NaN
        timestamp = converted_date.timestamp()
        return not math.isnan(timestamp)
    except (TypeError, ValueError, OSError):
        # to_date raises exceptions for invalid inputs
        return False
