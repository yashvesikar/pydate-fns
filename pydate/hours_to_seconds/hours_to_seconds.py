from math import trunc

SECONDS_IN_HOUR = 3600


def hours_to_seconds(hours: float) -> int:
    """
    Convert hours to seconds.

    :param hours: The number of hours to be converted
    :return: The number of hours converted in seconds

    Example:
        >>> hours_to_seconds(2)
        7200
    """
    return trunc(hours * SECONDS_IN_HOUR)