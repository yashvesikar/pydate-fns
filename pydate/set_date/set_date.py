
from datetime import datetime, timedelta
from typing import Union
import math
from ..to_date import to_date


def set_date(date: Union[datetime, int, float], day_of_month: Union[int, float]) -> datetime:
    """
    Set the day of the month to the given date.
    
    Set the day of the month to the given date. If the day is out of range for the month,
    it will overflow/underflow to adjacent months (matching JavaScript Date.setDate() behavior).
    
    Args:
        date: The date to be changed
        day_of_month: The day of the month of the new date
        
    Returns:
        The new date with the day of the month set
        
    Examples:
        >>> from datetime import datetime
        >>> # Set the 30th day of the month to 1 September 2014:
        >>> set_date(datetime(2014, 9, 1), 30)
        datetime.datetime(2014, 9, 30, 0, 0)
        >>> # Setting September 31 rolls over to October 1:
        >>> set_date(datetime(2014, 9, 1), 31)
        datetime.datetime(2014, 10, 1, 0, 0)
        >>> # Setting day 0 goes to last day of previous month:
        >>> set_date(datetime(2014, 9, 1), 0)
        datetime.datetime(2014, 8, 31, 0, 0)
    """
    # Handle NaN - return invalid datetime (matches JavaScript behavior)
    if isinstance(day_of_month, float) and math.isnan(day_of_month):
        # Create an invalid datetime by returning one with a NaN timestamp
        # This matches the JavaScript behavior where setDate(NaN) results in Invalid Date
        class InvalidDateTime(datetime):
            def timestamp(self):
                return float('nan')
        return InvalidDateTime(1970, 1, 1)
    
    dt = to_date(date)  # Will raise ValueError for invalid dates
    
    # JavaScript setDate() behavior: setting day 1 means first of month,
    # then we need to add (day_of_month - 1) days to handle overflow/underflow
    first_of_month = dt.replace(day=1)
    return first_of_month + timedelta(days=int(day_of_month) - 1)
