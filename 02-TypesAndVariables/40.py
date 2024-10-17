distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input("Enter fuel consumption per 100 km:"))
total_fuel_consumption = fuel_consumption * distance
total_cost = fuel_price * total_fuel_consumption
print(f"Total cost is {total_cost} dollars")