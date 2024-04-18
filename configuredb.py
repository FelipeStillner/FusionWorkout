import psycopg2

conn = psycopg2.connect(
    host="localhost", dbname="postgres", user="postgres", password="password", port=5432
)

cur = conn.cursor()

cur.execute(
    """CREATE TABLE IF NOT EXISTS users (
    email VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255),
    password VARCHAR(255),
    role CHAR
    );
    """
)

cur.execute(
    """INSERT INTO users (email, name, password, role) VALUES 
    ('client@gmail.com', 'Client', 'senha', 'C'),
    ('manager@gmail.com', 'Manager', '1234', 'M'), 
    ('personal@gmail.com', 'Personal', 'pass', 'P');
    """
)

conn.commit()

cur.close()
conn.close()
