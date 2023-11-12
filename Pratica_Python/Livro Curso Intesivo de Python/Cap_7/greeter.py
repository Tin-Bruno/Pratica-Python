def get_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()


ACTIVE = True
while ACTIVE:
    print('\nPlease tell me your name:')
    print('Enter "q" to quit')

    f_name = input('\nFirst name: ')
    if f_name == 'q':
        break

    l_neme = input('Last name: ')
    if l_neme == 'q':
        break

    formated_name = get_formatted_name(f_name, l_neme)

    print('\nHello, ' + formated_name + '!')
