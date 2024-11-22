cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]


def seats_total(cinema_seats):
    seats = 0
    for column in cinema_seats:
        for row in cinema_seats:
            seats += 1

    return seats

def seats_available(cinema_seats):
    available = 0
    taken = 0
    for row in cinema_seats:
        for element in row:
            if element == 'A':
                available += 1
            elif element == 'B':
                taken += 1

    return available, taken

def seat_status(cinema_seats, row, place):
    if cinema_seats[row - 1][place - 1] == 'A':
        return 'Available'
    elif cinema_seats[row - 1][place - 1] == 'B':
        return 'Taken'
    
print('CINEMA INFORMATION TABLE')
print('Total seats:',seats_total(cinema_seats))
print('Seats available/taken:',seats_available(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))