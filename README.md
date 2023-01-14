# pydate-fns

## A sensible Python date library

---

![PyPI - Downloads](https://img.shields.io/pypi/dm/pydate-fns)
![Code Climate coverage](https://img.shields.io/codeclimate/coverage/yashvesikar/pydate-fns)

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
- [ ] addMinutes
- [x] addMonths
- [ ] addQuarters
- [ ] addSeconds
- [x] addWeeks
- [x] addYears
- [ ] areIntervalsOverlapping
- [ ] clamp
- [ ] closestIndexTo
- [x] closestTo
- [ ] compareAsc
- [ ] compareDesc
- [ ] constants
- [ ] constructFrom
- [ ] daysToWeeks
- [ ] differenceInBusinessDays
- [ ] differenceInCalendarDays
- [ ] differenceInCalendarISOWeekYears
- [ ] differenceInCalendarISOWeeks
- [ ] differenceInCalendarMonths
- [ ] differenceInCalendarQuarters
- [ ] differenceInCalendarWeeks
- [ ] differenceInCalendarYears
- [ ] differenceInDays
- [ ] differenceInHours
- [ ] differenceInISOWeekYears
- [ ] differenceInMilliseconds
- [ ] differenceInMinutes
- [ ] differenceInMonths
- [ ] differenceInQuarters
- [ ] differenceInSeconds
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
- [ ] getDate
- [ ] getDay
- [ ] getDayOfYear
- [ ] getDaysInMonth
- [ ] getDaysInYear
- [ ] getDecade
- [ ] getDefaultOptions
- [ ] getHours
- [ ] getISODay
- [ ] getISOWeek
- [ ] getISOWeekYear
- [ ] getISOWeeksInYear
- [ ] getMilliseconds
- [ ] getMinutes
- [ ] getMonth
- [ ] getOverlappingDaysInIntervals
- [ ] getQuarter
- [ ] getSeconds
- [ ] getTime
- [ ] getUnixTime
- [ ] getWeek
- [ ] getWeekOfMonth
- [ ] getWeekYear
- [ ] getWeeksInMonth
- [ ] getYear
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
- [ ] startOfWeek
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
