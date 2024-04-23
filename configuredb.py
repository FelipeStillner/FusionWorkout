import psycopg2

conn = psycopg2.connect(
    host="localhost", dbname="postgres", user="postgres", password="password", port=5432
)

cur = conn.cursor()

cur.execute(
    """
    DROP TABLE IF EXISTS users;
    CREATE TABLE users (
        email VARCHAR(255) PRIMARY KEY,
        name VARCHAR(255),
        password VARCHAR(255),
        role CHAR
    );
    INSERT INTO users (email, name, password, role) VALUES 
        ('client@gmail.com', 'Client', 'senha', 'C'),
        ('a@a', 'a', 'a', 'C'),
        ('manager@gmail.com', 'Manager', '1234', 'M'), 
        ('personal@gmail.com', 'Personal', 'pass', 'P');
    """
)

cur.execute(
    """
    DROP TABLE IF EXISTS clients;
    CREATE TABLE clients (
        email VARCHAR(255) PRIMARY KEY,
        weeklyplan_id INT 
    );
    INSERT INTO clients (email, weeklyplan_id) VALUES 
        ('client@gmail.com', 1),
        ('a@a', 0);
    """
)

cur.execute(
    """
    DROP TABLE IF EXISTS weeklyplan;
    CREATE TABLE weeklyplan (
        id INT PRIMARY Key,
        name VARCHAR(255)
    );
    INSERT INTO weeklyplan (id, name) VALUES 
        (0, 'Fit'),
        (1, 'Maromba');
    """
)

conn.commit()

cur.close()
conn.close()
