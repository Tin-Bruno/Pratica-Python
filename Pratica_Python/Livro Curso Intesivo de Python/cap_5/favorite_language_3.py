favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python', }
print('The following have been mencioned:')
for language in set(favorite_languages.values()):
    print(language.title())
