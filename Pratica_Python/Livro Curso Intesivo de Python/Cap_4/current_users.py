current_users = ["bruno", "carlos", "daniel", "jorge", "maria",]
new_users = ["lucas", "michael", "pedro", "BRUNO", "carlos",]
for user in new_users:
    if user.lower() not in current_users:
        print("\tThe user " + user + " is available")
    if user.lower() in current_users:
        print("\tThe user " + user + " is not available")
