import sys


def add_time(start, duration, day=None):
    week = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']

  # Start part
    [hour_minute_part, suffix_part] = start.split(' ')
    [hourString, minuteString] = hour_minute_part.split(':')

    hourInt = int(hourString)
    minuteInt = int(minuteString)
    if suffix_part == 'PM':
        if hourInt != 12:
            hourInt += 12
    else:
        if hourInt == 12:
            hourInt = 0

    start_in_minutes = (hourInt * 60) + minuteInt
    next_day_leap_minutes = (24 * 60) - start_in_minutes

    # Duration part
    [durHourString, durMinuteString] = duration.split(':')

    durHourInt = int(durHourString)
    durMinuteInt = int(durMinuteString)
    dur_in_minutes = (durHourInt * 60) + durMinuteInt

    days_later = 0

    if dur_in_minutes > next_day_leap_minutes:
        minutes_total = (dur_in_minutes - next_day_leap_minutes)

        days_later = (minutes_total//1440) + 1
        minutes_later = (minutes_total % 1440)
        minuteInt = minutes_later % 60
        hourInt = minutes_later // 60
    else:
        hourInt += durHourInt
        minuteInt += durMinuteInt
        diff_hour_minutes = minuteInt - 60
        if diff_hour_minutes >= 0:
            hourInt += 1
            minuteInt = diff_hour_minutes

    if hourInt >= 12:
        suffix_part = 'PM'
        if hourInt != 12:
            hourInt -= 12
    else:
        suffix_part = 'AM'
        if hourInt == 0:
            hourInt = 12

    final_date = str(hourInt)+':'+str(minuteInt).rjust(2,
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


arguments = sys.argv

if len(arguments) < 3:
    print('Missing arguments, must insert "--start" and "--duration" arguments, "--day" is optional')

if len(arguments) == 5 and arguments[1] != '--start' or arguments[3] != '--duration':
    print('Argument "--start" and value of start is required as input for the script')
elif len(arguments) == 5:
    print(add_time(arguments[2], arguments[4]))
elif len(arguments) == 7:
    if arguments[5] == '--day':
        print(add_time(arguments[2], arguments[4]), arguments[6])
elif len(arguments) == 6:
    print('Value of "--day" missing')

# examples
# print(add_time('8:16 PM', '466:02', 'tuesday'))
# print(add_time('11:43 AM', '00:20'))
# print(add_time('11:30 AM', '2:32', 'Monday'))
