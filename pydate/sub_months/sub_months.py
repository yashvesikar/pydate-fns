import unittest
from datetime import datetime

from ..add_months import add_months


def sub_months(date: datetime, amount: int) -> datetime:
    """_summary_

    :param datetime date: _description_
    :return datetime: _description_
    """

    if not isinstance(date, datetime):
        raise TypeError("date must be of type datetime")
    elif not isinstance(amount, int):
        raise TypeError("amount must be of type int")

    return add_months(date, -amount)
