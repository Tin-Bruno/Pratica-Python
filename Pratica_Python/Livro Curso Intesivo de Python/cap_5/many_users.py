users = {'aeinstein': {'first': 'albert',
                       'last': 'einstein',
                       'location': 'princeton'},
         'mcurie': {'first': 'marie',
                    'last': 'curie',
                    'location': 'paris'}}
for username, user_info in users.items():
    print('\nUsername: ' + username.title())
    FULL_NAME = user_info['first'] + ' ' + user_info['last']
    LOCATION = user_info['location']
    print('Full name: ' + FULL_NAME.title()
          + '\n', 'Location: ' + LOCATION.title())
