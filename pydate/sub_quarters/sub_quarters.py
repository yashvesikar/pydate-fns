
from datetime import datetime
from typing import Union
from ..add_quarters import add_quarters


def sub_quarters(date: Union[datetime, int, float], amount: Union[int, float]) -> datetime:
    """
    Subtract the specified number of year quarters from the given date.
    
    Subtract the specified number of year quarters from the given date.
    
    Args:
        date: The date to be changed
        amount: The amount of quarters to be subtracted
        
    Returns:
        The new date with the quarters subtracted
        
    Examples:
        >>> from datetime import datetime
        >>> # Subtract 1 quarter from 1 December 2014:
        >>> sub_quarters(datetime(2014, 12, 1), 1)
        datetime.datetime(2014, 9, 1, 0, 0)
    """
    return add_quarters(date, -amount)
