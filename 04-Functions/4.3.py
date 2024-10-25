import math
def triangle_area(a,b,c):
    halfp = (a+b+c)/2
    area = math.sqrt(halfp*(halfp-a)*(halfp-b)*(halfp-c))
    return area

a = int(input('Enter side a: '))
b = int(input('Enter side b: '))
c = int(input('Enter side c: '))
print(f'The area of ​​a triangle with sides {a}, {b}, {c} is {triangle_area(a,b,c)}')