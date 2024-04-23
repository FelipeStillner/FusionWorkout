from Project.User import User
from Project.WeeklyPlan import WeeklyPlan


class Client(User):
    def __init__(self, email):
        super().__init__(email)
        self.plan = WeeklyPlan(email)

    def dbg(self):
        return f"plan: ({self.plan.dbg()}), super: ({super().dbg()})"
