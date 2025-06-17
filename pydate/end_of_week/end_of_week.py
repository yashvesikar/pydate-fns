
from datetime import datetime, timedelta
from typing import Union

from ..to_date.to_date import to_date


def end_of_week(date: Union[datetime, int, float], week_starts_on: int = 0) -> datetime:
    """
    Return the end of a week for the given date.
    
    The result will be in the local timezone with time set to 23:59:59.999999.

    :param date: The original date
    :param week_starts_on: The index of the first day of the week (0 - Sunday, 1 - Monday, etc.)
    :return datetime: The end of a week
    
    Examples:
        >>> from datetime import datetime
        >>> # End of week (Sunday-Saturday) for Tuesday Sept 2, 2014
        >>> result = end_of_week(datetime(2014, 9, 2, 11, 55, 0))
        >>> result == datetime(2014, 9, 6, 23, 59, 59, 999999)  # Saturday
        True
        
        >>> # End of week starting Monday for Tuesday Sept 2, 2014  
        >>> result = end_of_week(datetime(2014, 9, 2, 11, 55, 0), week_starts_on=1)
        >>> result == datetime(2014, 9, 7, 23, 59, 59, 999999)  # Sunday
        True
        
        >>> # Accepts timestamps
        >>> result = end_of_week(datetime(2014, 9, 2, 11, 55, 0).timestamp())
        >>> result == datetime(2014, 9, 6, 23, 59, 59, 999999)
        True
    """
    _date = to_date(date)
    current_day = _date.weekday()  # Monday is 0, Sunday is 6
    
    # Convert Python weekday to Sunday=0 format for consistency with date-fns
    if current_day == 6:  # Sunday
        current_day = 0
    else:
        current_day += 1  # Monday=1, Tuesday=2, etc.
    
    # Calculate days to add to reach end of week
    # End of week is 6 days after start of week
    days_to_add = (6 - (current_day - week_starts_on) + 7) % 7
    
    # Get end of week by adding days and setting to end of day
    result = _date + timedelta(days=days_to_add)
    return result.replace(hour=23, minute=59, second=59, microsecond=999999)
