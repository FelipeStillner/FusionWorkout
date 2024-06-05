import psycopg2
from Food import Food

class Diet:
    def __init__(self, id) -> None:
        self.foods = []
        self.clientid = id
    def print(self):
        print("clientid: "+id)
        for day in self.foods:
            for food in day:
                food.print()
        

