
from datetime import datetime
from typing import Union
from ..to_date import to_date


def start_of_quarter(date: Union[datetime, int, float]) -> datetime:
    """
    Return the start of a year quarter for the given date.
    
    Return the start of a year quarter for the given date.
    The result will be in the local timezone.
    
    Args:
        date: The original date
        
    Returns:
        The start of a quarter
        
    Examples:
        >>> from datetime import datetime
        >>> # The start of a quarter for 2 September 2014 11:55:00:
        >>> start_of_quarter(datetime(2014, 9, 2, 11, 55, 0))
        datetime.datetime(2014, 7, 1, 0, 0)
    """
    dt = to_date(date)
    
    # Quarters: Q1 = Jan-Mar (months 1-3), Q2 = Apr-Jun (4-6), 
    #           Q3 = Jul-Sep (7-9), Q4 = Oct-Dec (10-12)
    # Find the first month of the quarter
    current_month = dt.month
    # Python months are 1-based, so we need to adjust the calculation
    # For month 1,2,3 -> 1; 4,5,6 -> 4; 7,8,9 -> 7; 10,11,12 -> 10
    first_month_of_quarter = current_month - ((current_month - 1) % 3)
    
    # Set to the first day of the first month of the quarter at 00:00:00
    return dt.replace(
        month=first_month_of_quarter,
        day=1,
        hour=0,
        minute=0,
        second=0,
        microsecond=0
    )
