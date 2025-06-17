
import re
import math
from datetime import datetime
from typing import Union
from ..to_date import to_date
from ..is_valid import is_valid


def format(date: Union[datetime, int, float], format_str: str) -> str:
    """
    Format the date.
    
    Return the formatted date string in the given format.
    
    Format tokens:
    | Unit              | Pattern | Result examples             |
    |-------------------|---------|----------------------------|
    | Calendar year     | y       | 44, 1, 1900, 2017         |
    |                   | yy      | 44, 01, 00, 17            |
    |                   | yyyy    | 0044, 0001, 1900, 2017    |
    | Month             | M       | 1, 2, ..., 12             |
    |                   | MM      | 01, 02, ..., 12          |
    |                   | MMM     | Jan, Feb, ..., Dec        |
    |                   | MMMM    | January, February, ..., December |
    | Day of month      | d       | 1, 2, ..., 31             |
    |                   | dd      | 01, 02, ..., 31          |
    | Hour [0-23]       | H       | 0, 1, 2, ..., 23          |
    |                   | HH      | 00, 01, 02, ..., 23      |
    | Hour [1-12]       | h       | 1, 2, ..., 11, 12        |
    |                   | hh      | 01, 02, ..., 11, 12      |
    | Minute            | m       | 0, 1, ..., 59             |
    |                   | mm      | 00, 01, ..., 59          |
    | Second            | s       | 0, 1, ..., 59             |
    |                   | ss      | 00, 01, ..., 59          |
    | AM, PM            | a       | AM, PM                    |
    | Millisecond       | S       | 0, 1, ..., 9              |
    |                   | SS      | 00, 01, ..., 99          |
    |                   | SSS     | 000, 001, ..., 999       |
    
    Args:
        date: The original date
        format_str: The string of tokens
        
    Returns:
        The formatted date string
        
    Raises:
        ValueError: If date is invalid
        
    Examples:
        >>> from datetime import datetime
        >>> format(datetime(2014, 2, 11), 'MM/dd/yyyy')
        '02/11/2014'
        >>> format(datetime(2014, 7, 2, 15), "h 'o''clock'")
        "3 o'clock"
    """
    try:
        dt = to_date(date)
    except ValueError:
        raise ValueError("Invalid time value")
    
    if not is_valid(dt):
        raise ValueError("Invalid time value")
    
    # Month names
    month_names_short = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
                        
    month_names_long = ['January', 'February', 'March', 'April', 'May', 'June',
                       'July', 'August', 'September', 'October', 'November', 'December']
    
    # Format tokens regex - handle quoted strings first, then format tokens
    # Order matters: longer patterns first, then shorter ones
    token_regex = re.compile(r"'([^']|'')*'|''|MMMM|MMM|MM|yyyy|yy|dd|HH|hh|mm|ss|SSS|SS|M|y|d|H|h|m|s|S|a")
    
    def replace_token(match):
        token = match.group(0)
        
        # Handle quoted strings
        if token.startswith("'"):
            if token == "''":
                return "'"
            # Remove outer quotes and handle escaped quotes
            inner = token[1:-1] if token.endswith("'") else token[1:]
            return inner.replace("''", "'")
        
        # Year
        if token == 'yyyy':
            return f"{dt.year:04d}"
        elif token == 'yy':
            return f"{dt.year % 100:02d}"
        elif token == 'y':
            return str(dt.year)
            
        # Month
        elif token == 'MMMM':
            return month_names_long[dt.month - 1]
        elif token == 'MMM':
            return month_names_short[dt.month - 1]
        elif token == 'MM':
            return f"{dt.month:02d}"
        elif token == 'M':
            return str(dt.month)
            
        # Day
        elif token == 'dd':
            return f"{dt.day:02d}"
        elif token == 'd':
            return str(dt.day)
            
        # Hour (24-hour)
        elif token == 'HH':
            return f"{dt.hour:02d}"
        elif token == 'H':
            return str(dt.hour)
            
        # Hour (12-hour)
        elif token == 'hh':
            hour_12 = dt.hour % 12
            if hour_12 == 0:
                hour_12 = 12
            return f"{hour_12:02d}"
        elif token == 'h':
            hour_12 = dt.hour % 12
            if hour_12 == 0:
                hour_12 = 12
            return str(hour_12)
            
        # Minute
        elif token == 'mm':
            return f"{dt.minute:02d}"
        elif token == 'm':
            return str(dt.minute)
            
        # Second
        elif token == 'ss':
            return f"{dt.second:02d}"
        elif token == 's':
            return str(dt.second)
            
        # Millisecond
        elif token == 'SSS':
            return f"{dt.microsecond // 1000:03d}"
        elif token == 'SS':
            return f"{dt.microsecond // 10000:02d}"
        elif token == 'S':
            return str(dt.microsecond // 100000)
            
        # AM/PM
        elif token == 'a':
            return 'AM' if dt.hour < 12 else 'PM'
            
        # Return unchanged if not a recognized token
        else:
            return token
    
    # Replace tokens but preserve everything else
    result = []
    last_end = 0
    
    for match in token_regex.finditer(format_str):
        # Add any text before this match
        if match.start() > last_end:
            result.append(format_str[last_end:match.start()])
        
        # Add the replacement for this match
        result.append(replace_token(match))
        last_end = match.end()
    
    # Add any remaining text after the last match
    if last_end < len(format_str):
        result.append(format_str[last_end:])
    
    return ''.join(result)
