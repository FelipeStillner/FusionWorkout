from Project.DBManager import get_user


class User:

    def __init__(self, email):
        info = get_user(email)
        self.email = email
        self.name = info[0]
        self.role = info[1]

    def dbg(self):
        return f"email: ({self.email}), name: ({self.name}), role: ({self.role})"
