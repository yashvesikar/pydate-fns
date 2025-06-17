
from datetime import datetime
from typing import Union
from ..add_business_days import add_business_days


def sub_business_days(date: Union[datetime, int, float], amount: int) -> datetime:
    """
    Subtract the specified number of business days (Mon - Fri) from the given date.
    
    Subtract the specified number of business days from the given date, ignoring weekends.
    
    Args:
        date: The date to be changed
        amount: The amount of business days to be subtracted
        
    Returns:
        The new date with the business days subtracted
        
    Raises:
        ValueError: If amount is NaN
        
    Examples:
        >>> from datetime import datetime
        >>> # Subtract 10 business days from Monday September 15, 2014:
        >>> sub_business_days(datetime(2014, 9, 15), 10)
        datetime.datetime(2014, 9, 1, 0, 0)
    """
    return add_business_days(date, -amount)
