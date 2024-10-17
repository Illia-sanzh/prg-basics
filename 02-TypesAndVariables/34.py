import random
dice = random.randint(1,6)
is_special = dice == 1 or dice == 6
print(f"Dice is {dice}, is special: {is_special}")