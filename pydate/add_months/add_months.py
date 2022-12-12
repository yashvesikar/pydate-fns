from datetime import datetime, timedelta


def add_months(date: datetime, amount: int) -> datetime:
    """
    Add months to a date.
    :param date: The date to add months to.
    :param months: The number of months to add.
    :return:
    """
    if not isinstance(date, datetime):
        raise TypeError("date must be of type datetime")
    if not isinstance(amount, int):
        raise TypeError("months must be of type int")

    _months = date.month + amount
    _years = date.year + _months // 12
    _months = _months % 12

    # If the day of the month is greater than the number of days in the new month,
    # the day of the month is set to the last day of the new month.
    end_of_desired_month = datetime(_years, _months + 1, 1) - timedelta(days=1)
    if date.day > end_of_desired_month.day:
        return end_of_desired_month

    return date.replace(year=_years, month=_months)
