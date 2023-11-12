favorite_languages = {'jen': 'java',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python', }
friends = ['jen', 'sarah',]
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Hi "
              + name.title()
              + ", i see you favorite language is "
              + favorite_languages[name])
