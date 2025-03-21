from datetime import datetime, timedelta
from ..start_of_day.start_of_day import start_of_day

def start_of_tomorrow() -> datetime:
    """Return the start of tomorrow.

    Returns:
        The start of tomorrow.

    Example:
        >>> from datetime import datetime
        >>> # If today is 6 October 2014:
        >>> start_of_tomorrow()
        datetime(2014, 10, 7, 0, 0)
    """
    tomorrow = datetime.now() + timedelta(days=1)
    return start_of_day(tomorrow)