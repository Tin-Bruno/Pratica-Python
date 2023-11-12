people = {'Tin': {'firt_name': 'Bruno',
                  'last_name': 'Rodrigues',
                  'age': 18,
                  'city': 'São Paulo'},
          'Nice': {'firt_name': 'Nice',
                   'last_name': 'Moreira',
                   'age': 59,
                   'city': 'São Paulo'},
          'Henri': {'firt_name': 'Henrique',
                    'last_name': 'Rodrigues',
                    'age': 40,
                    'city': 'Divisopólis'}}
for username, user_info in people.items():
    print("\nUsername: ", username)
    FULL_NAME = user_info['firt_name'] + ' ' + user_info['last_name']
    AGE = user_info['age']
    CITY = user_info['city']
    print("\nFull name: ", FULL_NAME,
          "\nAge: ", AGE,
          "\nCity: ", CITY)
