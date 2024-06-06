import psycopg2
from Food import Food

class Diet:
    def __init__(self, id) -> None:
        self.clientid = id
        self.foods = [[], [], [], [], [], [], []]
        con = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="password", port=5432)
        cur = con.cursor()
        cur.execute('select id, day from "Food" where client_id = '+str(id)+'')
        infos = cur.fetchall()
        for info in infos:
            self.foods[info[1]].append(Food(info[0]))
        con.close()
    def print(self):
        print("clientid: "+id)
        for day in self.foods:
            for food in day:
                food.print()
        

