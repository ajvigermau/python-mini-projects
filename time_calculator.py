"""Importing sys modulw"""
import sys


def add_time(start, duration, day=None):
    """Function which handles time calculation ⏲"""
    week = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']

  # Start part
    [hour_minute_part, suffix_part] = start.split(' ')
    [hour_string, minute_string] = hour_minute_part.split(':')

    hour_int = int(hour_string)
    minute_int = int(minute_string)
    if suffix_part == 'PM':
        if hour_int != 12:
            hour_int += 12
    else:
        if hour_int == 12:
            hour_int = 0

    start_in_minutes = (hour_int * 60) + minute_int
    next_day_leap_minutes = (24 * 60) - start_in_minutes

    # Duration part
    [duration_hour_string, duration_minute_string] = duration.split(':')

    duration_hour_int = int(duration_hour_string)
    duration_minute_int = int(duration_minute_string)
    dur_in_minutes = (duration_hour_int * 60) + duration_minute_int

    days_later = 0

    if dur_in_minutes > next_day_leap_minutes:
        minutes_total = dur_in_minutes - next_day_leap_minutes

        days_later = (minutes_total//1440) + 1
        minutes_later = minutes_total % 1440
        minute_int = minutes_later % 60
        hour_int = minutes_later // 60
    else:
        hour_int += duration_hour_int
        minute_int += duration_minute_int
        diff_hour_minutes = minute_int - 60
        if diff_hour_minutes >= 0:
            hour_int += 1
            minute_int = diff_hour_minutes

    if hour_int >= 12:
        suffix_part = 'PM'
        if hour_int != 12:
            hour_int -= 12
    else:
        suffix_part = 'AM'
        if hour_int == 0:
            hour_int = 12

    final_date = str(hour_int)+':'+str(minute_int).rjust(2,
                                                         '0') + ' ' + suffix_part

    if day:
        current_day_index = week.index(day.capitalize())
        current_day = week[current_day_index]
        actual_day_index = week.index(current_day) + days_later
        if actual_day_index <= 6:
            actual_day = week[actual_day_index]
        else:
            actual_day_index = week.index(current_day) + (days_later % 5 - 1)
        actual_day = week[actual_day_index]
        final_date += ', ' + str(actual_day)

    if days_later != 0:
        if days_later == 1:
            final_date += ' (next day)'
        else:
            final_date += ' ('f'{days_later}' + ' days later)'

    return final_date


script_arguments = sys.argv

# Remove first element of collection that usually is script
script_arguments.pop(0)

if "--start" not in script_arguments:
    print("[ERROR] Missing argument --start")
    sys.exit(1)

start_value_index = script_arguments.index("--start") + 1

if len(script_arguments) < (start_value_index + 1):
    print("[ERROR] Argument --start value not provided")
    sys.exit(1)

start_value = script_arguments[start_value_index]

if "--duration" not in script_arguments:
    print("[ERROR] Missing argument --duration")
    sys.exit(1)

duration_value_index = script_arguments.index("--duration") + 1

if len(script_arguments) < (duration_value_index + 1):
    print("[ERROR] Argument --duration value not provided")
    sys.exit(1)

duration_value = script_arguments[duration_value_index]

if "--day" in script_arguments:
    day_value_index = script_arguments.index("--day") + 1
    if len(script_arguments) < (day_value_index + 1):
        print("[ERROR] Argument --day value not provided")
        sys.exit(1)
    else:
        day_value = script_arguments[day_value_index]

time = add_time(start_value, duration_value, day_value)

print(time)
