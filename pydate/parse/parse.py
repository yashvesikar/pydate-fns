
import re
from datetime import datetime
from typing import Union


def parse(date_string: str, format_str: str, reference_date: Union[datetime, int, float] = None) -> datetime:
    """
    Parse the date from string using the given format string.
    
    This is a basic implementation that handles common format patterns.
    For complex parsing scenarios, consider using dateutil.parser or similar libraries.
    
    Supported format tokens:
    | Unit              | Pattern | Examples               |
    |-------------------|---------|------------------------|
    | Calendar year     | yyyy    | 2014, 0044, 1900      |
    |                   | yy      | 14, 44, 00            |
    |                   | y       | 2014, 44, 1900        |
    | Month             | MM      | 01, 02, 12            |
    |                   | M       | 1, 2, 12              |
    |                   | MMM     | Jan, Feb, Dec         |
    |                   | MMMM    | January, February     |
    | Day of month      | dd      | 01, 02, 31            |
    |                   | d       | 1, 2, 31              |
    | Hour [0-23]       | HH      | 00, 01, 23            |
    |                   | H       | 0, 1, 23              |
    | Hour [1-12]       | hh      | 01, 02, 12            |
    |                   | h       | 1, 2, 12              |
    | Minute            | mm      | 00, 01, 59            |
    |                   | m       | 0, 1, 59              |
    | Second            | ss      | 00, 01, 59            |
    |                   | s       | 0, 1, 59              |
    | AM, PM            | a       | AM, PM                |
    | Millisecond       | SSS     | 000, 001, 999         |
    
    Args:
        date_string: The string to parse
        format_str: The format string
        reference_date: Reference date for missing components (defaults to current date)
        
    Returns:
        The parsed datetime object
        
    Raises:
        ValueError: If the string doesn't match the format or is invalid
        
    Examples:
        >>> parse('2014-02-11', 'yyyy-MM-dd')
        datetime.datetime(2014, 2, 11, 0, 0)
        >>> parse('02/11/14', 'MM/dd/yy')
        datetime.datetime(2014, 2, 11, 0, 0)
        >>> parse('3:30 PM', 'h:mm a')
        datetime.datetime(1900, 1, 1, 15, 30)
    """
    if reference_date is None:
        reference_date = datetime.now()
    elif isinstance(reference_date, (int, float)):
        reference_date = datetime.fromtimestamp(reference_date)
    
    # Month name mappings
    month_names_short = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month_names_long = ['January', 'February', 'March', 'April', 'May', 'June',
                       'July', 'August', 'September', 'October', 'November', 'December']
    
    # Create mapping dictionaries
    month_short_map = {name: i+1 for i, name in enumerate(month_names_short)}
    month_long_map = {name: i+1 for i, name in enumerate(month_names_long)}
    
    # Start with reference date components
    year = reference_date.year
    month = reference_date.month
    day = reference_date.day
    hour = 0
    minute = 0
    second = 0
    microsecond = 0
    is_pm = False
    hour_12_format = False
    
    # Build regex pattern from format string
    pattern_parts = []
    format_tokens = []
    
    # Token regex to find format tokens in the format string
    token_regex = re.compile(r"'([^']|'')*'|''|MMMM|MMM|MM|yyyy|yy|dd|HH|hh|mm|ss|SSS|M|y|d|H|h|m|s|a")
    
    last_end = 0
    
    for match in token_regex.finditer(format_str):
        # Add literal text before this token
        if match.start() > last_end:
            literal = format_str[last_end:match.start()]
            pattern_parts.append(re.escape(literal))
        
        token = match.group(0)
        format_tokens.append(token)
        
        # Convert format token to regex pattern
        if token.startswith("'"):
            # Quoted literal text
            if token == "''":
                pattern_parts.append("'")
            else:
                inner = token[1:-1] if token.endswith("'") else token[1:]
                pattern_parts.append(re.escape(inner.replace("''", "'")))
        elif token == 'yyyy':
            pattern_parts.append(r'(\d{4})')
        elif token == 'yy':
            pattern_parts.append(r'(\d{2})')
        elif token == 'y':
            pattern_parts.append(r'(\d{1,4})')
        elif token == 'MMMM':
            pattern_parts.append(r'(' + '|'.join(month_names_long) + ')')
        elif token == 'MMM':
            pattern_parts.append(r'(' + '|'.join(month_names_short) + ')')
        elif token == 'MM':
            pattern_parts.append(r'(\d{2})')
        elif token == 'M':
            pattern_parts.append(r'(\d{1,2})')
        elif token == 'dd':
            pattern_parts.append(r'(\d{2})')
        elif token == 'd':
            pattern_parts.append(r'(\d{1,2})')
        elif token == 'HH':
            pattern_parts.append(r'(\d{2})')
        elif token == 'H':
            pattern_parts.append(r'(\d{1,2})')
        elif token == 'hh':
            pattern_parts.append(r'(\d{2})')
        elif token == 'h':
            pattern_parts.append(r'(\d{1,2})')
        elif token == 'mm':
            pattern_parts.append(r'(\d{2})')
        elif token == 'm':
            pattern_parts.append(r'(\d{1,2})')
        elif token == 'ss':
            pattern_parts.append(r'(\d{2})')
        elif token == 's':
            pattern_parts.append(r'(\d{1,2})')
        elif token == 'SSS':
            pattern_parts.append(r'(\d{3})')
        elif token == 'a':
            pattern_parts.append(r'(AM|PM)')
        else:
            # Unknown token, treat as literal
            pattern_parts.append(re.escape(token))
        
        last_end = match.end()
    
    # Add remaining literal text
    if last_end < len(format_str):
        pattern_parts.append(re.escape(format_str[last_end:]))
    
    # Combine into full regex pattern
    full_pattern = '^' + ''.join(pattern_parts) + '$'
    
    # Match the string against the pattern
    match = re.match(full_pattern, date_string)
    if not match:
        raise ValueError(f"String '{date_string}' does not match format '{format_str}'")
    
    # Extract values and apply them
    groups = match.groups()
    group_index = 0
    
    for token in format_tokens:
        # Skip quoted strings - they don't produce capture groups
        if token.startswith("'"):
            continue
            
        if token in ['MMMM', 'MMM', 'MM', 'M', 'yyyy', 'yy', 'y', 
                     'dd', 'd', 'HH', 'H', 'hh', 'h', 'mm', 'm', 
                     'ss', 's', 'SSS', 'a']:
            if group_index < len(groups):
                value = groups[group_index]
                group_index += 1
                
                if token == 'yyyy':
                    year = int(value)
                elif token == 'yy':
                    year_val = int(value)
                    # Convert 2-digit year (assume 1900-2099 range)
                    if year_val < 50:
                        year = 2000 + year_val
                    else:
                        year = 1900 + year_val
                elif token == 'y':
                    year = int(value)
                elif token == 'MMMM':
                    month = month_long_map[value]
                elif token == 'MMM':
                    month = month_short_map[value]
                elif token in ['MM', 'M']:
                    month = int(value)
                elif token in ['dd', 'd']:
                    day = int(value)
                elif token in ['HH', 'H']:
                    hour = int(value)
                elif token in ['hh', 'h']:
                    hour = int(value)
                    hour_12_format = True
                elif token in ['mm', 'm']:
                    minute = int(value)
                elif token in ['ss', 's']:
                    second = int(value)
                elif token == 'SSS':
                    microsecond = int(value) * 1000
                elif token == 'a':
                    is_pm = value == 'PM'
    
    # Adjust hour for 12-hour format
    if hour_12_format:
        if is_pm and hour != 12:
            hour += 12
        elif not is_pm and hour == 12:
            hour = 0
    
    # Validate ranges
    if not (1 <= month <= 12):
        raise ValueError(f"Invalid month: {month}")
    if not (1 <= day <= 31):
        raise ValueError(f"Invalid day: {day}")
    if not (0 <= hour <= 23):
        raise ValueError(f"Invalid hour: {hour}")
    if not (0 <= minute <= 59):
        raise ValueError(f"Invalid minute: {minute}")
    if not (0 <= second <= 59):
        raise ValueError(f"Invalid second: {second}")
    
    try:
        return datetime(year, month, day, hour, minute, second, microsecond)
    except ValueError as e:
        raise ValueError(f"Invalid date components: {e}")
