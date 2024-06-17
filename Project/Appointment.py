import psycopg2

class Appointment:
    def __init__(self, id):
        con = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="password", port=5432)
        cur = con.cursor()
        cur.execute('select * from "Appointment" where id = '+str(id)+'')
        info = cur.fetchone()
        self.id = info[0]
        self.clientid = info[1]
        self.date = info[2]
        self.personalid = info[3]
        self.time = info[4]
        con.close()
    def print(self):
        print("id: "+str(self.id)+", clientid: "+self.clientid+", date: "+self.date+", personalid: "+self.personalid+", time: "+self.time)
    def from_client(user_id):
        con = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="password", port=5432)
        cur = con.cursor()
        cur.execute(f'select id from "Appointment" where client_id = {user_id} OR client_id is NULL')
        infos = cur.fetchall()
        con.close()
        result = []
        for info in infos:
            result.append(Appointment(info[0]))
        return result
    def from_personal(user_id):
        con = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="password", port=5432)
        cur = con.cursor()
        cur.execute(f'select id from "Appointment" where personal_id = {user_id}')
        infos = cur.fetchall()
        con.close()
        result = []
        for info in infos:
            result.append(Appointment(info[0]))
        return result
    def all():
        con = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="password", port=5432)
        cur = con.cursor()
        cur.execute(f'select id from "Appointment"')
        infos = cur.fetchall()
        con.close()
        result = []
        for info in infos:
            result.append(Appointment(info[0]))
        return result
    def add(date, personal_id, time):
        con = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="password", port=5432)
        cur = con.cursor()
        cur.execute('INSERT INTO public."Appointment"( client_id, date, personal_id, "time") VALUES ('+"NULL"+', \''+str(date)+'\', '+str(personal_id)+', \''+str(time)+'\');')
        con.commit()
        con.close()