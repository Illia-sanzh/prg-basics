basic_salary = 5000
total_salary = 0
is_bonus = True
bonus = 1.3

if is_bonus == True:
    total_salary = basic_salary * bonus
else:
    total_salary = basic_salary

print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary}')