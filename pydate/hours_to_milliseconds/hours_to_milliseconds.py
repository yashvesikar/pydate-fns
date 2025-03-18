from math import trunc

MILLISECONDS_IN_HOUR = 3600000


def hours_to_milliseconds(hours: float) -> int:
    """
    Convert hours to milliseconds.

    :param hours: number of hours to be converted
    :return: The number of hours converted to milliseconds

    Example:
        >>> hours_to_milliseconds(2)
        7200000
    """
    return trunc(hours * MILLISECONDS_IN_HOUR)