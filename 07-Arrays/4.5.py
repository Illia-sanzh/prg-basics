arr = [-15, 8, -31, 47, -2, 19]
min = float('inf')
max = float('-inf')
for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i]
    if arr[i] < min:
        min = arr[i]

print(min)
print(max)