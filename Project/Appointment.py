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
        cur.execute(f'select id from "Appointment" where client_id = {user_id}')
        infos = cur.fetchall()
        con.close()
        result = []
        for info in infos:
            result.append(Appointment(info(0)))
        return result
      