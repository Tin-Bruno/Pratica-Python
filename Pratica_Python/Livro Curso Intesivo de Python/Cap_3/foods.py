my_foods: list[str] = ['pizza', 'falafel', 'carrot', 'cake',]
friend_foods = my_foods[:]
my_foods.append(
    'cannoli')
friend_foods.append(
    'ice cream')
for food in my_foods:
    print("\nmy favorite food is " + food + ".\n")
for food in friend_foods:
    print("\nfriend's favorite food is " + food + ".\n")
print("\nthe three fist itens are:")
print(my_foods[0:3])
print("\nthe last three items is:")
print(my_foods[-3:])
