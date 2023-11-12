responses = {}
POLING_ACTIVE = True
while POLING_ACTIVE:
    name = input("\nWhat is your name? ")
    response = input("\nwhich moutain would you like to climb someday? ")
    responses[name] = response
    repeat = input("\nWould you like to let another person respond? (y/n)")

    if repeat == 'n':
        POLING_ACTIVE = False

    print("\n--- Poll results ---")

    for name, respose in responses.items():
        print(name.title()
              + " Wonld like to climb "
              + respose.title()
              + '.')
