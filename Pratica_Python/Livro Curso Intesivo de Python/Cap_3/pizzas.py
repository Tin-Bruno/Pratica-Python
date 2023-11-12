pizzas = ['catupiri', 'calabresa', 'mosarela',]
pizzas.append("peperone")
friends_pizzas = pizzas[:]
friends_pizzas.append('margherita')
print("list one:")
print(pizzas)
print("\nlist two:")
print(friends_pizzas)
for pizza in pizzas:
    print('\nmy favorite pizzas are: ' + pizza.title() + '.\n')
for pizza in friends_pizzas:
    print('\nmy friends favorite pizzas are: ' + pizza.title() + '.')
