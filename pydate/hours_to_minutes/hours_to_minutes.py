from math import trunc

MINUTES_IN_HOUR = 60


def hours_to_minutes(hours: float) -> int:
    """
    Convert hours to minutes.

    :param hours: The number of hours to be converted
    :return: The number of hours converted in minutes

    Example:
        >>> hours_to_minutes(2)
        120
    """
    return trunc(hours * MINUTES_IN_HOUR)