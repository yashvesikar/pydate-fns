from datetime import datetime

from ..to_naive import to_naive


def is_future(date: datetime) -> bool:
    """
    Is the given date in the future?
    :param datetime date: datetime object
    :return bool: True if the given date is in the future, False otherwise
    """

    if not isinstance(date, datetime):
        raise TypeError("date must be an instance of datetime")

    date = to_naive(date)

    return date.timestamp() > datetime.utcnow().timestamp()
