from datetime import datetime


def is_after(date: datetime, date_to_compare: datetime) -> bool:
    """
    Check if date is after date_to_compare.
    :param date: datetime object
    :param date_to_compare: datetime object to compare
    :return: bool
    """

    return date.timestamp() > date_to_compare.timestamp()
