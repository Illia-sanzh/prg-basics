import queue

def dec_to_bin(num):
    binary = queue.LifoQueue()
    while num != 0:
        if num%2 == 1:
            binary.put(1)
        else:
            binary.put(0)
        num = num // 2
    binarytot = ''
    while not binary.empty():
        number = binary.get()
        binarytot += str(number)

    return binarytot
num = 1023013901
print(f'Number is {num}, Binary is {dec_to_bin(num)}')

