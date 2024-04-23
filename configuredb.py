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

cur.execute(
    """
    DROP TABLE IF EXISTS dailyplan;
    CREATE TABLE dailyplan (
        weeklyplan_id INT,
        day INT,
        name VARCHAR(255)
    );
    INSERT INTO dailyplan (weeklyplan_id, day, name) VALUES 
        (0, 1, '1 F'),
        (0, 2, '2 F'),
        (0, 3, '3 F'),
        (0, 4, '4 F'),
        (0, 5, '5 F'),
        (0, 6, '6 F'),
        (0, 7, '7 F'),
        (1, 1, '1 M'),
        (1, 2, '2 M'),
        (1, 3, '3 M'),
        (1, 4, '4 M'),
        (1, 5, '5 M'),
        (1, 6, '6 M'),
        (1, 7, '7 M');
    """
)

cur.execute(
    """
    DROP TABLE IF EXISTS circuit;
    CREATE TABLE circuit (
        weekly_id INT,
        day INT,
        number INT,
        name VARCHAR(255)
    );
    INSERT INTO circuit (weekly_id, day, number, name) VALUES 
        (0, 1, 0, 'barra'),
        (0, 1, 1, 'flexao'),
        (0, 1, 2, 'boxe'),
        (0, 2, 0, 'karate'),
        (0, 2, 1, 'natacao');
    """
)

conn.commit()

cur.close()
conn.close()
