unconfirmed_users = ['alice', 'bob', 'carol', 'dave', 'emily']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying " + current_user.title())
    confirmed_users.append(current_user)
    print("\nThe folowing users have been verified.")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title() + " has been verified.")
