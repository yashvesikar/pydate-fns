from datetime import datetime


def is_before(date: datetime, date_to_compare: datetime) -> bool:
    """
    Check if date is after date_to_compare.
    :param date: datetime object
    :param date_to_compare: datetime object to compare
    :return: bool
    """

    if not isinstance(date, datetime) or not isinstance(date_to_compare, datetime):
        raise TypeError("date and date_to_compare must be of type datetime")

    return date.timestamp() < date_to_compare.timestamp()
