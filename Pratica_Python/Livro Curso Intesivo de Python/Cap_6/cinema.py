prompt = '\nPor favor informe sua idade:'
prompt += "\nDigite 'Quit' para sair."
while True:
    tickt_price = input(prompt)
    if tickt_price.lower() == 'quit':
        break
    elif int(tickt_price) < 3:
        print("\nSeu ingresso é gratuito!")
    elif int(tickt_price) <= 12:
        print("\nSeu ingresso custa 10 dolares!")
    else:
        print("\nSeu ingresso custa 15 dolares!")
