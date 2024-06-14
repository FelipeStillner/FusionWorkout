import psycopg2

class Workout:
    def __init__(self, id) -> None:
        con = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="password", port=5432)
        cur = con.cursor()
        cur.execute('select * from "Workout" where id = '+str(id)+'')
        info = cur.fetchone()
        con.close()
        self.id = info[0]
        self.circuit_id = info[1]
        self.name = info[2]
        self.repetitions = info[3]
        self.duration = info[4]
    def print(self):
        print("id: "+str(self.id)+", circuit_id: "+str(self.circuit_id)+", name: "+str(self.name)+", repetitions: "+self.repetitions+", duration: "+str(self.duration))
        

