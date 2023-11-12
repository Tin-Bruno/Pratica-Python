message = "\nPor favor adicione um ingrediente a pizza:"
message += "\nDigite 'Quit' para sair."
ACTIVE = True
while ACTIVE:
    ingrediente = input(message)
    if ingrediente.lower() == 'quit':
        ACTIVE = False
    else:
        print("\nO ingrediente "
              + ingrediente.title()
              + " foi adicionado a pizza!")
