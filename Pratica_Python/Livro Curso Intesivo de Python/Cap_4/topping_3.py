request_toppings = []
if request_toppings:
    for request_topping in request_toppings:
        print("adding "
              + request_topping
              + ".")
        print("\nFinished making your pizza!")
else:
    print("Are you sure want a plain pizza?")
