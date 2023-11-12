def get_format_name(firt_name, last_name, middle_name=''):
    if middle_name:
        full_name = firt_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = firt_name + ' ' + last_name
    return full_name.title()


MUSICIAN = get_format_name('johh', 'hooker', 'lee')
print(MUSICIAN)
