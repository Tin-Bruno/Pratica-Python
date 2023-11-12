hollyday = {}
ACTIVE = True
while ACTIVE:
    name = input("\nQual seu nome? ")
    question = input("\nSe pudesse visitar um lugar do mundo, para onde você iria?")
    hollyday[name] = question
    repeat = input("\nDeseja continuar? [S/N] ")

    if repeat.lower() == "n":
        ACTIVE = False

    print("\n___ Resutados ____")

    for name, question in hollyday.items():
        print(name.title()
              + ' gostaria de viajar para '
              + question.title())
