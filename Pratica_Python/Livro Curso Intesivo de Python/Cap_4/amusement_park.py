age = 20
if age < 4:
    PRICE = 0
elif age < 18:
    PRICE = 5
elif age < 65:
    PRICE = 10
else:
    PRICE = 5
print("Your admisson cost is $" + str(PRICE) + '.')
