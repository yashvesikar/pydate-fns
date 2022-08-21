from datetime import datetime


def add_months(date: datetime, months: int) -> datetime:
    """
    Add months to a date.
    :param date: The date to add months to.
    :param months: The number of months to add.
    :return:
    """
    if type(date) != datetime:
        raise TypeError("date must be of type datetime")
    if type(months) != int:
        raise TypeError("months must be of type int")
    if months < 0:
        raise ValueError("months must be greater than 0")

    _months = date.month + months
    _years = date.year + _months // 12
    _months = _months % 12
    return date.replace(year=_years, month=_months)
