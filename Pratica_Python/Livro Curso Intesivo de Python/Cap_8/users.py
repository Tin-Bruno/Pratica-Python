"""Pratica sobre classes"""


class Users():
    """Uma simples classe que representa um usuário"""

    def __init__(self, firt_nome, last_name, age, location):
        self.firt_name = firt_nome
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        """Descrição do usuário"""

        print("\nFull name: " + self.firt_name + " " + self.last_name)
        print("Your age is: " + str(self.age))
        print("Your location is: " + self.location)

    def greet_user(self):
        """Cumprimenta o usuário"""

        print("\nHello, " + self.firt_name + " " + self.last_name)

    def increment_login_attempts(self):
        """Atualiza o número de acesso de usuário"""

        self.login_attempts += 1
        print("\nYou have " + str(self.login_attempts) + " attempts left")

    def reset_login_attempts(self):
        """Reinicia o número de acesso de usuário"""

        self.login_attempts = 0


class Admin(Users):
    """Administ."""

    def __init__(self, firt_nome, last_name, age, location):
        """Initializa o usuário(ADNIM)."""

        super().__init__(firt_nome, last_name, age, location)
        self.privilege = Privileges()


class Privileges():
    """Privileges for admin."""

    privilege = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Monstra os privilegios do admin."""

        privilege = ["can add post", "can delete post", "can ban user"]

        print("\nThe privileges for admin is: " + str(privilege))


firt_user = Users("John", "Doe", 43, "Estados unidos")

firt_user.describe_user()
firt_user.greet_user()
firt_user.increment_login_attempts()
firt_user.increment_login_attempts()
firt_user.increment_login_attempts()
firt_user.increment_login_attempts()
firt_user.reset_login_attempts()
firt_user.increment_login_attempts()

user_admin = Admin("Bruno", "David", 18, "Brazil")

user_admin.describe_user()
user_admin.greet_user()
user_admin.privilege.show_privileges()
