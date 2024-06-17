import psycopg2
from Circuit import Circuit

class ExercisePlan:
    def __init__(self, id) -> None:
        self.clientid = id
        self.circuits = [[], [], [], [], [], [], []]
        con = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="password", port=5432)
        cur = con.cursor()
        cur.execute('select id, day from "Circuit" where client_id = '+str(id)+'')
        infos = cur.fetchall()
        for info in infos:
            self.circuits[info[1]].append(Circuit(info[0]))
        con.close()
    def print(self):
        print("clientid: "+id)
        for day in self.circuits:
            for c in day:
                c.print()

