def sum(num):
    summ = 0
    num = abs(num)
    stringnum = str(num)
    for i in range(len(stringnum)):
        summ += int(stringnum[i])
    return summ
num = int(input('Enter number: '))
print(sum(num))