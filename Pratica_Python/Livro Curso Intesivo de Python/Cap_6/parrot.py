prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
ACTIVE = True
while ACTIVE:
    message = input(prompt.lower())
    if message.lower() == 'quit':
       ACTIVE = False

    else:
        print(message)
