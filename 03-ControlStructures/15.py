month = int(input('Enter month number (1..12): '))
day = int(input('Enter the day number of the month: '))
day_okay = False
if month==1 or month==3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    if 1 <= day <= 31:
        day_ok = True
elif month == 4 or month == 6 or month == 9 or month == 11 :
    if 1 <= day <= 30:
        day_ok = True
elif month == 2:
    if 1 <= day <= 28:
        day_ok = True


if day_ok == True:
    print(f'Date {day} for month {month} is correct')
else:
    print('Day is incorrect')