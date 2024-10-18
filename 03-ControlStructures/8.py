number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))
operator = input("Enter operator: ")
match operator:
    case '+':
        total = number1 + number2
    case '-':
        total = number1 - number2
    case '*':
        total = number1 * number2
    case '/':
        total = number1 / number2
    case _:
        print("Wrong symbol")
print(f"Your operator was {operator}, Your total is {total}")