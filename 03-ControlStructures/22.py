total_sum = 0
amount = 0
while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  
    total_sum += number
    amount += 1


print(f"The total sum of the numbers is: {total_sum}")
print(f'The arithmetic mean is {total_sum/amount}')