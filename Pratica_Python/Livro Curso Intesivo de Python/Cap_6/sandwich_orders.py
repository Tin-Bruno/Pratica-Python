sandwich_orders = ['presunto', 'pastami', 'salad', 'bacon',
                   'pastami', 'cheese', 'meat', 'pastami']
finally_sandwiches = []
while 'pastami' in sandwich_orders:
    print("Sorry, we don't have that sandwich for Pastami.")
    sandwich_orders.remove('pastami')

while sandwich_orders:
    making_sandwich = sandwich_orders.pop()
    print("Sandwich makeing: ", making_sandwich.title())

    finally_sandwiches.append(making_sandwich)
    print("\nFinally sandwiches:")

    for finally_sandwich in finally_sandwiches:
        print(finally_sandwich.title() + " to be served")
