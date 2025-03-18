from math import trunc

MILLISECONDS_IN_MINUTE = 60000


def minutes_to_milliseconds(minutes: float) -> int:
    """
    Convert minutes to milliseconds.

    :param minutes: The number of minutes to be converted
    :return: The number of minutes converted in milliseconds

    Example:
        >>> minutes_to_milliseconds(2)
        120000
    """
    return trunc(minutes * MILLISECONDS_IN_MINUTE)