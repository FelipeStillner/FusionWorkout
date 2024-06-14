import psycopg2
from User import User
from Diet import Diet
from ExercisePlan import ExercisePlan

class Client(User):
    def __init__(self, id) -> None:
        super().__init__(id)
        con = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="password", port=5432)
        cur = con.cursor()
        cur.execute('select * from "Client" where id = '+str(id)+'')
        info = cur.fetchone()
        self.weight = info[1]
        self.height = info[2]
        self.sex = info[3]
        self.diet = Diet(id)
        self.exercise_plan = ExercisePlan(id)
        con.close()
    def new(email, name, password, weight, height, female):
        con = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="password", port=5432)
        cur = con.cursor()
        cur.execute('INSERT INTO "User"(email, name, password, kind) VALUES (\''+email+'\', \''+name+'\', \''+password+'\', \'C\');')
        con.commit()
        con.close()
        validate = User.validate(email, password)
        if validate[0]:
            id = validate[1]
            sex = "M"
            if female:
                sex = "F"
            con = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="password", port=5432)
            cur = con.cursor()
            cur.execute('INSERT INTO public."Client"(id, "weight (Kg)", "height (cm)", sex) VALUES (\''+str(id)+'\', \''+str(weight)+'\', \''+str(height)+'\', \''+sex+'\');')
            con.commit()
            con.close()
            return True
        return False
    def print(self):
        print("id: "+str(self.id)+", email: "+self.email+", name: "+self.name+", password: "+self.password+", kind: "+self.kind+", weight: "+self.weight+", height: "+self.height+", sex: "+self.sex)
        

