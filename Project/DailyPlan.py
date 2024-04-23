from Project.DBManager import get_dailyplan


class DailyPlan:
    def __init__(self, weeklyid, day):
        planinfo = get_dailyplan(weeklyid, day)
        self.weeklyid = planinfo[0]
        self.day = planinfo[1]
        self.name = planinfo[2]

    def dbg(self):
        return f"weeklyid: ({self.weeklyid}), day: ({self.day}), name: ({self.name})"
