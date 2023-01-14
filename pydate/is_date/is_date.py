from datetime import datetime


def is_date(date: datetime) -> bool:
    """
    Returns true if the given value is an instance of datetime.

    :param datetime date: datetime object
    :return bool: Returns true if the given value is an instance of datetime, False otherwise
    """
    return isinstance(date, datetime)
