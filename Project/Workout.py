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
    def add(circuit_id, name, repet, dur):
        con = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="password", port=5432)
        cur = con.cursor()
        cur.execute('INSERT INTO public."Workout"( circuit_id, name, repetitions, duration) VALUES ('+str(circuit_id)+', \''+str(name)+'\', '+str(repet)+', \''+str(dur)+'\');')
        con.commit()
        con.close()
    def remove(id):
        con = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="password", port=5432)
        cur = con.cursor()
        cur.execute('DELETE FROM public."Workout" WHERE id = '+str(id)+';')
        con.commit()
        con.close()  

