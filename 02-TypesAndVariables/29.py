import math

circ = int(input('Enter circumference:'))
radius = circ/(2*math.pi)
cut_down = radius >= 25
print(f'Radius is {radius}, tree can be cut down: {cut_down}')