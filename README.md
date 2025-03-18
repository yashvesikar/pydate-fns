# pydate-fns

## A sensible Python date library

---

![PyPI - Downloads](https://img.shields.io/pypi/dm/pydate-fns)
![Code Climate coverage](https://img.shields.io/codeclimate/coverage/yashvesikar/pydate-fns)

## Implementation Notes

### Assumptions and Decisions

1. DateTime Handling:
   - All functions accept both datetime objects and timestamps (float/int)
   - NaN values are handled gracefully, returning NaN for comparison functions
   - Timestamps are treated as UTC timestamps for consistency

2. Testing:
   - Each function has comprehensive test coverage matching the JavaScript implementation
   - Edge cases are explicitly tested (NaN, invalid dates, etc.)

3. API Differences from date-fns:
   - Python's datetime is used instead of JavaScript's Date object
   - Some JavaScript-specific features (like Date.now()) are adapted to Python equivalents

### Known Issues and Limitations

1. Timezone handling may differ slightly from date-fns due to Python's datetime behavior
2. Some JavaScript-specific date formatting options may not be available in Python

### Implementation Details

1. Timezone Handling:
   - For calendar day calculations, we convert dates to UTC to ensure consistent behavior
   - DST transitions are handled by using timestamp-based calculations and rounding
   - All timezone-sensitive operations normalize dates to avoid edge cases

2. Comparison Functions:
   - Comparison results match JavaScript's behavior (-1, 0, 1)
   - NaN handling follows JavaScript conventions
   - Timestamp comparisons use millisecond precision for consistency

3. Date Arithmetic:
   - Calendar day calculations account for DST transitions
   - Day boundaries are determined using start_of_day in UTC
   - Month calculations use year and month components directly
   - Calendar month differences ignore day of month and time components
   - Minute and second arithmetic uses timedelta for accurate DST handling
   - Week calculations support configurable week start (0-6 for Sunday-Saturday)
   - Invalid dates return datetime(1,1,1) instead of JavaScript's Invalid Date

4. Date Component Access:
   - Maintain Python's conventions (e.g., months 1-12) while implementing JavaScript logic
   - Invalid date inputs return NaN for numeric getters
   - Getters preserve timezone information from input dates
   - Documentation clearly states Python's conventions where they differ from JavaScript
   - Timestamp functions handle both seconds (Unix time) and milliseconds (JS time)
   - Microseconds are properly converted to milliseconds where needed

## Installation

```bash
pip install pydate-fns
```

## Usage

```python
from datetime import datetime
from pydate import is_weekday,

if is_weekday(datetime.now()):
    print("It's a weekday")
else:
    print("It's the weekend 😎")
```

<details>
    <summary>date-fns methods parity</summary>
    <!-- methods -->

### method

---

- [x] add
- [ ] addBusinessDays
- [x] addDays
- [x] addHours
- [ ] addISOWeekYears
- [x] addMilliseconds
- [x] addMinutes
- [x] addMonths
- [ ] addQuarters
- [x] addSeconds
- [x] addWeeks
- [x] addYears
- [ ] areIntervalsOverlapping
- [ ] clamp
- [ ] closestIndexTo
- [x] closestTo
- [x] compareAsc
- [x] compareDesc
- [ ] constants
- [ ] constructFrom
- [ ] daysToWeeks
- [ ] differenceInBusinessDays
- [x] differenceInCalendarDays
- [ ] differenceInCalendarISOWeekYears
- [ ] differenceInCalendarISOWeeks
- [x] differenceInCalendarMonths
- [ ] differenceInCalendarQuarters
- [x] differenceInCalendarWeeks
- [ ] differenceInCalendarYears
- [ ] differenceInDays
- [ ] differenceInHours
- [ ] differenceInISOWeekYears
- [x] differenceInMilliseconds
- [ ] differenceInMinutes
- [ ] differenceInMonths
- [ ] differenceInQuarters
- [x] differenceInSeconds
- [ ] differenceInWeeks
- [ ] differenceInYears
- [ ] eachDayOfInterval
- [ ] eachHourOfInterval
- [ ] eachMinuteOfInterval
- [ ] eachMonthOfInterval
- [ ] eachQuarterOfInterval
- [ ] eachWeekOfInterval
- [ ] eachWeekendOfInterval
- [ ] eachWeekendOfMonth
- [ ] eachWeekendOfYear
- [ ] eachYearOfInterval
- [ ] endOfDay
- [ ] endOfDecade
- [ ] endOfHour
- [ ] endOfISOWeek
- [ ] endOfISOWeekYear
- [ ] endOfMinute
- [ ] endOfMonth
- [ ] endOfQuarter
- [ ] endOfSecond
- [ ] endOfToday
- [ ] endOfTomorrow
- [ ] endOfWeek
- [ ] endOfYear
- [ ] endOfYesterday
- [ ] format
- [ ] formatDistance
- [ ] formatDistanceStrict
- [ ] formatDistanceToNow
- [ ] formatDistanceToNowStrict
- [ ] formatDuration
- [ ] formatISO
- [ ] formatISO9075
- [ ] formatISODuration
- [ ] formatRFC3339
- [ ] formatRFC7231
- [ ] formatRelative
- [ ] fp
- [ ] fromUnixTime
- [x] getDate
- [ ] getDay
- [ ] getDayOfYear
- [ ] getDaysInMonth
- [ ] getDaysInYear
- [ ] getDecade
- [ ] getDefaultOptions
- [x] getHours
- [ ] getISODay
- [ ] getISOWeek
- [ ] getISOWeekYear
- [ ] getISOWeeksInYear
- [x] getMilliseconds
- [x] getMinutes
- [x] getMonth
- [ ] getOverlappingDaysInIntervals
- [ ] getQuarter
- [x] getSeconds
- [x] getTime
- [x] getUnixTime
- [ ] getWeek
- [ ] getWeekOfMonth
- [ ] getWeekYear
- [ ] getWeeksInMonth
- [x] getYear
- [ ] hoursToMilliseconds
- [ ] hoursToMinutes
- [ ] hoursToSeconds
- [ ] intervalToDuration
- [ ] intlFormat
- [ ] intlFormatDistance
- [x] isAfter
- [x] isBefore
- [x] isDate
- [x] isEqual
- [x] isExists
- [x] isFirstDayOfMonth
- [x] isFriday
- [ ] isFuture
- [x] isLastDayOfMonth
- [x] isLeapYear
- [ ] isMatch
- [x] isMonday
- [ ] isPast
- [x] isSameDay
- [x] isSameHour
- [ ] isSameISOWeek
- [ ] isSameISOWeekYear
- [x] isSameMinute
- [x] isSameMonth
- [ ] isSameQuarter
- [ ] isSameSecond
- [ ] isSameWeek
- [x] isSameYear
- [x] isSaturday
- [x] isSunday
- [ ] isThisHour
- [ ] isThisISOWeek
- [ ] isThisMinute
- [ ] isThisMonth
- [ ] isThisQuarter
- [ ] isThisSecond
- [ ] isThisWeek
- [ ] isThisYear
- [x] isThursday
- [ ] isToday
- [ ] isTomorrow
- [x] isTuesday
- [ ] isValid
- [x] isWednesday
- [ ] isWeekend
- [ ] isWithinInterval
- [ ] isYesterday
- [ ] lastDayOfDecade
- [ ] lastDayOfISOWeek
- [ ] lastDayOfISOWeekYear
- [ ] lastDayOfMonth
- [ ] lastDayOfQuarter
- [ ] lastDayOfWeek
- [ ] lastDayOfYear
- [ ] lightFormat
- [ ] locale
- [ ] max
- [ ] milliseconds
- [ ] millisecondsToHours
- [ ] millisecondsToMinutes
- [ ] millisecondsToSeconds
- [ ] min
- [ ] minutesToHours
- [ ] minutesToMilliseconds
- [ ] minutesToSeconds
- [ ] monthsToQuarters
- [ ] monthsToYears
- [ ] nextDay
- [ ] nextFriday
- [ ] nextMonday
- [ ] nextSaturday
- [ ] nextSunday
- [ ] nextThursday
- [ ] nextTuesday
- [ ] nextWednesday
- [ ] parse
- [ ] parseISO
- [ ] parseJSON
- [ ] previousDay
- [ ] previousFriday
- [ ] previousMonday
- [ ] previousSaturday
- [ ] previousSunday
- [ ] previousThursday
- [ ] previousTuesday
- [ ] previousWednesday
- [ ] quartersToMonths
- [ ] quartersToYears
- [ ] roundToNearestMinutes
- [ ] secondsToHours
- [ ] secondsToMilliseconds
- [ ] secondsToMinutes
- [ ] set
- [ ] setDate
- [ ] setDay
- [ ] setDayOfYear
- [ ] setDefaultOptions
- [ ] setHours
- [ ] setISODay
- [ ] setISOWeek
- [ ] setISOWeekYear
- [ ] setMilliseconds
- [ ] setMinutes
- [ ] setMonth
- [ ] setQuarter
- [ ] setSeconds
- [ ] setWeek
- [ ] setWeekYear
- [ ] setYear
- [x] startOfDay
- [ ] startOfDecade
- [x] startOfHour
- [ ] startOfISOWeek
- [ ] startOfISOWeekYear
- [ ] startOfMinute
- [ ] startOfMonth
- [ ] startOfQuarter
- [ ] startOfSecond
- [ ] startOfToday
- [ ] startOfTomorrow
- [x] startOfWeek
- [ ] startOfWeekYear
- [ ] startOfYear
- [ ] startOfYesterday
- [x] sub
- [ ] subBusinessDays
- [x] subDays
- [ ] subHours
- [ ] subISOWeekYears
- [ ] subMilliseconds
- [ ] subMinutes
- [x] subMonths
- [ ] subQuarters
- [ ] subSeconds
- [ ] subWeeks
- [ ] subYears
- [x] toDate
- [ ] transpose
- [ ] weeksToDays
- [ ] yearsToMonths
- [ ] yearsToQuarters
      <!-- /methods -->
      </details>
