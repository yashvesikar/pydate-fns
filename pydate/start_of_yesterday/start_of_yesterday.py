from datetime import datetime, timedelta
from ..start_of_day.start_of_day import start_of_day

def start_of_yesterday() -> datetime:
    """Return the start of yesterday.

    Returns:
        The start of yesterday.

    Example:
        >>> from datetime import datetime
        >>> # If today is 6 October 2014:
        >>> start_of_yesterday()
        datetime(2014, 10, 5, 0, 0)
    """
    yesterday = datetime.now() - timedelta(days=1)
    return start_of_day(yesterday)