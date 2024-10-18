driving_mode = input('Enter driving mode (A/M/E): ')
distance = int(input('Enter distance in km: '))

match driving_mode:
    case 'A':
        fuel_consumption = 7
    case 'M':
        fuel_consumption = 9
    case 'E':
        fuel_consumption = 6
    case _:
        print("Wrong symbol")

total_consumption = fuel_consumption * (distance/100)
print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption} liters')