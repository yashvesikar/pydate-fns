from datetime import datetime
from decimal import Decimal
from typing import Union


def to_date(dirty_date: Union[datetime, int, float, Decimal]) -> datetime:
    """
    Convert a dirty date to a datetime object.
    :param dirty_date: The dirty date to convert.
    :return: The datetime object.
    :raises TypeError: If dirty_date is not of type datetime, int, float, or Decimal
    :raises ValueError: If dirty_date is NaN
    """
    if isinstance(dirty_date, datetime):
        return dirty_date
    elif isinstance(dirty_date, (int, float)):
        if isinstance(dirty_date, float) and dirty_date != dirty_date:  # NaN check
            raise ValueError("Cannot convert NaN to datetime")
        return datetime.fromtimestamp(dirty_date)
    elif isinstance(dirty_date, Decimal):
        return datetime.fromtimestamp(float(dirty_date))
    else:
        raise TypeError("dirty_date must be of type datetime, int, float, or Decimal")
