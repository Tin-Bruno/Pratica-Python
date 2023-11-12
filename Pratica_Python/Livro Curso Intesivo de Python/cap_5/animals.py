pets = {'Tobi': {'animal': 'dog',
                 'owner': 'leidiane'},
        'Mari': {'animal': 'cat',
                 'owner': 'nice'},
        'Simba': {'animal': 'dog',
                  'owner': 'henrigue'}}
for name, pet in pets.items():
    print('Name is :' + name
          + '\n', '\tAnimal is :', pet['animal']
          + '\n', '\tOwner is :', pet['owner'])
