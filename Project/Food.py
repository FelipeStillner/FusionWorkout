import psycopg2

class Food:
    def __init__(self, id) -> None:
        con = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="password", port=5432)
        cur = con.cursor()
        cur.execute('select * from "Food" where id = '+str(id)+'')
        info = cur.fetchone()
        con.close()
        self.id = info[0]
        self.clientid = info[1]
        self.day = info[2]
        self.name = info[3]
        self.quantity = info[4]
        self.energy = info[5]
    def print(self):
        print("id: "+str(self.id)+", clinetid: "+str(self.clientid)+", day: "+str(self.day)+", name: "+self.name+", quantity: "+str(self.quantity)+", energy: "+str(self.energy))
        

