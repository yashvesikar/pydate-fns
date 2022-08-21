from datetime import datetime
from decimal import Decimal
from typing import Union


def to_date(dirty_date: Union[int, float, Decimal]) -> datetime:
    """
    Convert a dirty date to a datetime object.
    :param dirty_date: The dirty date to convert.
    :return: The datetime object.
    """

    if isinstance(dirty_date, int) or isinstance(dirty_date, float):
        return datetime.fromtimestamp(dirty_date)
    elif isinstance(dirty_date, Decimal):
        return datetime.fromtimestamp(float(dirty_date))
    else:
        raise TypeError("dirty_date must be of type int, float, or Decimal")
