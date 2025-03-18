from math import trunc

MILLISECONDS_IN_SECOND = 1000


def seconds_to_milliseconds(seconds: float) -> int:
    """
    Convert seconds to milliseconds.

    :param seconds: The number of seconds to be converted
    :return: The number of seconds converted in milliseconds

    Example:
        >>> seconds_to_milliseconds(2)
        2000
    """
    return trunc(seconds * MILLISECONDS_IN_SECOND)