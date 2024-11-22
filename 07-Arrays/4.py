arr = [2, 3, 7, 5, 4]
string = ''
print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Last value', arr[-1])
print('Last but one value', arr[len(arr) - 2])
print('Sum of first and last values', arr[0] + arr[-1])
print('Middle value', arr[len(arr)//2])

for i in range(len(arr)):
    string += str(arr[i]) + ' '
print(string)
    
