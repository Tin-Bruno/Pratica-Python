favorite_languages = {'jen': 'java', 'sarah': 'c',
                      'edward': 'ruby', 'phil': 'python'}
persons = ['bruno', 'david', 'jen']
for person in persons:
    if person not in favorite_languages:
        print(person.title() + ', Would you to answer this poll?')
    if person in favorite_languages:
        print(person.title() + ', Thank for to answer the poll!')
