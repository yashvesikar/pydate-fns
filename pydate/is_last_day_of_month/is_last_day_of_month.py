from datetime import datetime, timedelta


def is_last_day_of_month(date: datetime) -> bool:
    """
    Is the given date the last day of a month?

    :param datetime date: datetime object
    :return bool: True if the date is the last day of a month, False otherwise
    """
    if not isinstance(date, datetime):
        raise TypeError("date must be a datetime object")

    return date.month != (date + timedelta(days=1)).month
