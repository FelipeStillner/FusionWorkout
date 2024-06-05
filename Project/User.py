import psycopg2

class User:
    def __init__(self, id) -> None:
        con = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="password", port=5432)
        cur = con.cursor()
        cur.execute('select * from "User" where id = '+str(id)+'')
        info = cur.fetchone()
        con.close()
        self.id = id
        self.name = info[2]
        self.email = info[1]
        self.password = info[3]
        self.kind = info[4]
    def validate(email, password):
        con = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="password", port=5432)
        cur = con.cursor()
        cur.execute('select * from "User" where email = \''+email+'\'')
        info = cur.fetchone()
        con.close()
        if not (info is None):
            if password == info[3]: 
                return True, info[0]
        return False, -1
    def print(self):
        print("id: "+str(self.id)+", email: "+self.email+", name: "+self.name+", password: "+self.password+", kind: "+self.kind)
        