from datetime import datetime, timedelta
from typing import Union
import math
from ..to_date import to_date


def add_months(date: Union[datetime, int, float], amount: Union[int, float]) -> datetime:
    """
    Add months to a date.
    :param date: The date to add months to.
    :param amount: The number of months to add.
    :return: The new date with the months added.
    """
    dt = to_date(date)
    
    # Handle NaN amount
    if isinstance(amount, float) and math.isnan(amount):
        raise ValueError("Amount cannot be NaN")
    
    if not isinstance(amount, (int, float)):
        raise TypeError("months must be of type int or float")
    
    amount = int(amount)

    # Calculate total months and handle the 0-based vs 1-based month issue
    total_months = dt.month - 1 + amount  # Convert to 0-based for calculation
    _years = dt.year + total_months // 12
    _months = (total_months % 12) + 1  # Convert back to 1-based

    # Handle negative months
    if _months <= 0:
        _years -= 1
        _months += 12

    # Get the last day of the target month
    if _months == 12:
        next_month_first = datetime(_years + 1, 1, 1)
    else:
        next_month_first = datetime(_years, _months + 1, 1)
    
    end_of_desired_month = next_month_first - timedelta(days=1)
    
    # If the day exceeds the target month's days, use the last day
    if dt.day > end_of_desired_month.day:
        return end_of_desired_month.replace(
            hour=dt.hour,
            minute=dt.minute,
            second=dt.second,
            microsecond=dt.microsecond
        )

    return dt.replace(year=_years, month=_months)
