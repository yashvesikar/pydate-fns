
from datetime import datetime, timedelta
from typing import Union
from ..to_date import to_date


def end_of_quarter(date: Union[datetime, int, float]) -> datetime:
    """
    Return the end of a year quarter for the given date.
    
    Return the end of a year quarter for the given date.
    The result will be in the local timezone.
    
    Args:
        date: The original date
        
    Returns:
        The end of a quarter
        
    Examples:
        >>> from datetime import datetime
        >>> # The end of a quarter for 2 September 2014 11:55:00:
        >>> end_of_quarter(datetime(2014, 9, 2, 11, 55, 0))
        datetime.datetime(2014, 9, 30, 23, 59, 59, 999999)
    """
    dt = to_date(date)
    
    # Quarters: Q1 = Jan-Mar (months 1-3), Q2 = Apr-Jun (4-6), 
    #           Q3 = Jul-Sep (7-9), Q4 = Oct-Dec (10-12)
    # Find the last month of the quarter
    current_month = dt.month
    # For month 1,2,3 -> 3; 4,5,6 -> 6; 7,8,9 -> 9; 10,11,12 -> 12
    last_month_of_quarter = current_month - ((current_month - 1) % 3) + 2
    
    # Get the first day of the next month, then subtract one day
    if last_month_of_quarter == 12:
        # December -> next January
        next_month_first = datetime(dt.year + 1, 1, 1)
    else:
        next_month_first = datetime(dt.year, last_month_of_quarter + 1, 1)
    
    # Go back one day to get the last day of the quarter month
    last_day = next_month_first - timedelta(days=1)
    
    # Set time to 23:59:59.999999
    return last_day.replace(
        hour=23,
        minute=59,
        second=59,
        microsecond=999999
    )
