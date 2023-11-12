def greet_users(names):
    for name in names:
        msg = 'Hello, ' + name.title() + '!'
        print(msg)


username = ['hanna', 'jessica', 'kate']
greet_users(username)
