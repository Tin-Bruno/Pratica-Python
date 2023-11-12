cars = {'toyota': {'cost': 200000},
        'bmw': {'cost': 250000},
        'honda': {'cost': 350000},
        'subaru': {'cost': 400000},
        'supra': {'cost': 450000}}
search = input("what car would you like to search for? ")
if search in cars:
    print(f"{search.title()} We have the car")
    Price = input("Would you to know the cost of the car?")
    if Price == 'yes':
        print(f"{search.title()} costs {cars[search]['cost']}")
    else:
        print("ok")
else:
    print(f"Sorry, we don't have {search.title()}")
