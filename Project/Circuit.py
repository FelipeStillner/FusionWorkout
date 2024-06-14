import psycopg2
from Workout import Workout

class Circuit:
    def __init__(self, id) -> None:
        con = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="password", port=5432)
        cur = con.cursor()
        cur.execute('select * from "Circuit" where id = '+str(id)+'')
        info = cur.fetchone()
        con.close()
        self.id = info[0]
        self.client_id = info[1]
        self.day = info[2]
        self.name = info[3]
        self.repetitions = info[4]
        self.workouts = []
        con = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="password", port=5432)
        cur = con.cursor()
        cur.execute('select id from "Workout" where circuit_id = '+str(id)+'')
        infos = cur.fetchall()
        for info in infos:
            self.workouts.append(Workout(info[0]))
        con.close()
        
    def print(self):
        print("id: "+str(self.id)+", clien_tid: "+str(self.client_id)+", day: "+str(self.day)+", name: "+self.name+", repetitions: "+str(self.repetitions))
        for w in self.workouts:
                w.print()
        

