number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 10 == 0:
    print("The number " + str(number) + " is multiplo of teen.")
else:
    print("The number " + str(number) + " is not multiplo of teen.")
