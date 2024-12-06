
price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

total = 0
for key, value in price_list.items():
    print(key, value)
    total += value

print(total)
total = total* 0.9
print(total)

total_disc = 0
for key, value in price_list.items():
    value = value * 0.9
    price_list[key] = value
    total_disc += value
print(total_disc)
print(price_list)