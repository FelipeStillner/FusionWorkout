from Project.DBManager import get_dailyplan
from Project.DBManager import get_circuits
from Project.Circuit import Circuit


class DailyPlan:
    def __init__(self, weeklyid, day):
        planinfo = get_dailyplan(weeklyid, day)
        self.weeklyid = planinfo[0]
        self.day = planinfo[1]
        self.name = planinfo[2]
        self.circuits = list()
        circuitsinfo = get_circuits(weeklyid, day)
        for info in circuitsinfo:
            self.circuits.append(Circuit(weeklyid, day, info[0], info[1]))

    def dbg(self):
        return f"weeklyid: ({self.weeklyid}), day: ({self.day}), name: ({self.name})"
