from datetime import datetime


def is_exists(year: int, month: int, day: int) -> bool:
    """
    Checks if the given arguments convert to an existing date.

    :param int year: year of the date to check
    :param int month: month of the date to check
    :param int day: day of the date to check
    :return bool: True if the given arguments convert to an existing date, False otherwise
    """
    try:
        datetime(year, month, day)
        return True
    except (ValueError, TypeError) as e:
        print(e)
        return False
