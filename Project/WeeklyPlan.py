from Project.DBManager import get_weeklyplan
from Project.DailyPlan import DailyPlan


class WeeklyPlan:
    def __init__(self, email):
        planinfo = get_weeklyplan(email)
        self.id = planinfo[0]
        self.name = planinfo[1]
        self.dailies = list()
        for i in range(1, 8):
            self.dailies.append(DailyPlan(self.id, i))

    def dbg(self):
        s = f"id: ({self.id}), name: ({self.name})"
        for dayli in self.dailies:
            s = s + "\n" + dayli
        return s
