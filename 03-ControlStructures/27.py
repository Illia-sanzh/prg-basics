park_time = int(input("Enter hours spent in parking: "))
match park_time:
    case park_time if park_time >= 6:
        print('20 PLN')
    case park_time if park_time >= 3:
        print('15 PLN')
    case park_time if park_time > 0:
        print('5 PLN')
