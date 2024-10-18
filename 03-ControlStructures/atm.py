import time
balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("5.Check pin")
    print('6.Change your pin')

    choice = input("Choose an option (1-6): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    elif choice == '5':
        print(f'Your pin is {pin}')
    elif choice == '6':
        print(f'Your pin is {pin}')
        new_pin = (input('Enter your new pin: '))
        if new_pin.isdigit() == True:
            pin = int(new_pin)
            print(f"Your new pin is {pin}")

        else:
            print("Sorry. You entered characters into your pin")
            continue
    else:
        print("Invalid option. Please try again.")
