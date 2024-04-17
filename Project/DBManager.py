import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="password", port=5432)

def authenticate_user(email, password):
    cur = conn.cursor()
    cur.execute(f"""SELECT password FROM users WHERE email = '{email}'""")
    right = cur.fetchone()[0]
    conn.commit()
    cur.close()
    
    if password == right:
        return True
    return False
    
def create_user(email, name, password, role):
    cur = conn.cursor()
    cur.execute(f"""INSERT INTO users (email, name, password, role) VALUES 
    ('{email}', '{name}', '{password}', '{role}');
    """)
    conn.commit()
    cur.close()