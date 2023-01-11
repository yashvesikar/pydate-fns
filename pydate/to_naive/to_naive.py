from datetime import datetime
from zoneinfo import ZoneInfo

utc = ZoneInfo("UTC")


def to_naive(date: datetime) -> datetime:
    """
    Convert a datetime object to a naive datetime object.

    :param datetime date: datetime object (potentially aware)
    :return datetime: naive datetime object
    """
    if not isinstance(date, datetime):
        raise TypeError("date must be an instance of datetime")

    if date.tzinfo is None:
        return date

    # convert to utc and remove tzinfo
    return date.astimezone(utc).replace(tzinfo=None)
