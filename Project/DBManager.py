import psycopg2

conn = psycopg2.connect(
    host="localhost", dbname="postgres", user="postgres", password="password", port=5432
)


def authenticate_user(email, password):
    right = None
    cur = conn.cursor()
    cur.execute(f"""SELECT password FROM users WHERE email = '{email}'""")
    for i in cur.fetchall():
        right = i[0]
    conn.commit()
    cur.close()
    print(right)
    if password == right:
        return True
    return False


def create_user(email, name, password, role):
    try:
        cur = conn.cursor()
        cur.execute(
            f"""INSERT INTO users (email, name, password, role) VALUES 
        ('{email}', '{name}', '{password}', '{role}');
        """
        )
        conn.commit()
        cur.close()
        return True
    except:
        return False


def get_user(email):
    cur = conn.cursor()
    cur.execute(f"""SELECT name, role FROM users WHERE email = '{email}'""")
    for i in cur.fetchall():
        user = i
    conn.commit()
    cur.close()
    return user


def get_weeklyplan(email):
    cur = conn.cursor()
    cur.execute(f"""SELECT weeklyplan_id FROM clients WHERE email = '{email}'""")
    for i in cur.fetchall():
        id = i
    conn.commit()
    cur.close()
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM weeklyplan WHERE id = '{id[0]}'""")
    for i in cur.fetchall():
        planinfo = i
    conn.commit()
    cur.close()
    return planinfo


def get_dailyplan(weeklyid, day):
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM dailyplan WHERE weeklyplan_id = {weeklyid} AND day = {day}""")
    for i in cur.fetchall():
        dailyinfo = i
    conn.commit()
    cur.close()
    return dailyinfo

def get_circuits(weeklyid, day):
    circuitsinfo = list()
    cur = conn.cursor()
    cur.execute(f"""SELECT number, name FROM circuit WHERE weekly_id = {weeklyid} and day = {day}""")
    for i in cur.fetchall():
        circuitsinfo.append(i)
    conn.commit()
    cur.close()
    return circuitsinfo
