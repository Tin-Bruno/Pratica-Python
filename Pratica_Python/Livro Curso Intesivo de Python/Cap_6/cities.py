prompt = "\nPleace enter name of a city you have visited: "
prompt += "\nEnter 'quit' to exit: "
while True:
    city = input(prompt)
    if city.lower() == 'quit':
        break
    print("I'love to go to " + city.title() + "!")
