arr = [34, 7, 19, 4, 21, 8]

i = 0
evencount = 0
while(i < len(arr)):
    if arr[i] % 2 == 0:
        evencount += 1
    i += 1

print(evencount)