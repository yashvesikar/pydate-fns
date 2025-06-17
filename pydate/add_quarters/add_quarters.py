
from datetime import datetime
from typing import Union
import math
from ..to_date import to_date
from ..add_months import add_months


def add_quarters(date: Union[datetime, int, float], amount: Union[int, float]) -> datetime:
    """
    Add the specified number of year quarters to the given date.
    
    Add the specified number of year quarters to the given date.
    
    Args:
        date: The date to be changed
        amount: The amount of quarters to be added
        
    Returns:
        The new date with the quarters added
        
    Examples:
        >>> from datetime import datetime
        >>> # Add 1 quarter to 1 September 2014:
        >>> add_quarters(datetime(2014, 9, 1), 1)
        datetime.datetime(2014, 12, 1, 0, 0)
    """
    # Handle NaN amount
    if isinstance(amount, float) and math.isnan(amount):
        raise ValueError("Amount cannot be NaN")
    
    # Convert amount to int if it's a float
    if isinstance(amount, float):
        amount = int(amount)
    
    return add_months(date, amount * 3)
