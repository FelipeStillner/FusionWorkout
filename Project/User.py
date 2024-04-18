from Project.DBManager import get_user


class User:
    def __init__(self, email):
        user = get_user(email)
        self.email = email
        print(user)
        self.name = user[0]
        self.role = user[1]

    def dbg(self):
        return f"email: {self.email}, name: {self.name}, role: {self.role}, "
