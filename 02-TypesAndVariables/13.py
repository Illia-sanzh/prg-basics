a = int(input("Enter length:"))
b = int(input("Enter width:"))
c = int(input("Enter height:"))
volume = a*b*c
surface_area = ((a+b)*2)*c + (a*b)*2
print(f'Volume is {volume}, surface area is {surface_area}')