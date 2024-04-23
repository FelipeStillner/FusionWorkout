from Project.DBManager import get_plan


class WeeklyPlan:
    def __init__(self, email):
        planinfo = get_plan(email)
        self.id = planinfo[0]
        self.name = planinfo[1]

    def dbg(self):
        return f"id: ({self.id}), name: ({self.name})"
