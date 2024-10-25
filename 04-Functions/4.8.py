def time_string(hour, minute, format):
    if format == 12 and hour < 12:
        time = (f'{hour}:{minute:02}am')
    elif format == 12 and hour > 12:
        time = (f'{hour%12}:{minute:02}pm')
    elif format == 12 and hour == 12:
        time = (f'{12}:{minute:02}pm')
    elif format == 24:
        time = (f'{hour:02}:{minute:02}')
    return time

hour = int(input('Enter hour: '))
minute = int(input('Enter minutes: '))
format = int(input('Enter format: '))

print(time_string(hour, minute, format))

