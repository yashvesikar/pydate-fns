from datetime import datetime
from typing import Union, Optional
import math
from ..to_date import to_date
from ..start_of_week import start_of_week


def get_week_year(date: Union[datetime, int, float], week_starts_on: Optional[int] = None, first_week_contains_date: Optional[int] = None) -> Union[int, float]:
    """
    Get the local week-numbering year of the given date.
    
    Get the local week-numbering year of the given date.
    The exact calculation depends on the values of
    week_starts_on (which is the index of the first day of the week)
    and first_week_contains_date (which is the day of January, which is always in
    the first week of the week-numbering year)
    
    Args:
        date: The given date
        week_starts_on: Which day of the week is the first day of the week (0=Sunday, 1=Monday, etc.)
        first_week_contains_date: The day of January, which is always in the first week of the week-numbering year
        
    Returns:
        The local week-numbering year
        
    Examples:
        >>> from datetime import datetime
        >>> # Which week numbering year is 26 December 2004 with the default settings?
        >>> get_week_year(datetime(2004, 12, 26))
        2005
    """
    try:
        dt = to_date(date)
        
        # Handle NaN input date
        if math.isnan(dt.timestamp()):
            return float('nan')
            
        # Default settings
        if week_starts_on is None:
            week_starts_on = 0
        if first_week_contains_date is None:
            first_week_contains_date = 1
            
        year = dt.year
        
        # Create first week of next year
        first_week_of_next_year = datetime(year + 1, 1, first_week_contains_date)
        start_of_next_year = start_of_week(first_week_of_next_year, week_starts_on)
        
        # Create first week of this year
        first_week_of_this_year = datetime(year, 1, first_week_contains_date)
        start_of_this_year = start_of_week(first_week_of_this_year, week_starts_on)
        
        # Compare timestamps
        if dt >= start_of_next_year:
            return year + 1
        elif dt >= start_of_this_year:
            return year
        else:
            return year - 1
            
    except (ValueError, TypeError, OSError):
        return float('nan')