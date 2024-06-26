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
    def add(client_id, day, name, quant, cal):
        con = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="password", port=5432)
        cur = con.cursor()
        cur.execute('INSERT INTO public."Food"( client_id, day, name, "quantity (g)", "energy (cal)") VALUES ('+str(client_id)+', '+str(day)+', \''+str(name)+'\', '+str(quant)+', '+str(cal)+');')
        con.commit()
        con.close()
    def remove(id):
        con = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="password", port=5432)
        cur = con.cursor()
        cur.execute('DELETE FROM public."Food" WHERE id = '+str(id)+';')
        con.commit()
        con.close()

