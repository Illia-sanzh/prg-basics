# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

sum_food = 0
sum_tran = 0
sum_uti = 0
week1 = 0
week2 = 0
week3 = 0
week4 = 0
for i in range(len(monthly_expenses)):
    sum_food += monthly_expenses[i][0]
    sum_tran += monthly_expenses[i][1]
    sum_uti += monthly_expenses[i][2]
for j in range(len(monthly_expenses[0])):
    week1 += monthly_expenses[0][j]
    week2 += monthly_expenses[1][j]
    week3 += monthly_expenses[2][j]
    week4 += monthly_expenses[3][j]

total = week1 + week2 +week3 +week4
print(week1)
# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',sum_food)
print('Transport:',sum_tran)
print('Utilities:',sum_uti)
print('Week 1:',week1)
print('Week 2:',week2)
print('Week 3:', week3)
print('Week 4:', week4)
print('---------------')
print('TOTAL:',total)