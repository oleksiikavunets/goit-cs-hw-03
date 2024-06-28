import random

import psycopg2
from faker import Faker


def generate_data():
    statuses = [('new',), ('in progress',), ('completed',)]
    users = [(Faker().name(), Faker().email()) for _ in range(10)]
    tasks = [(Faker().catch_phrase(), Faker().text(), random.choice(statuses), random.choice(users)[1]) for _ in
             range(50)]
    return statuses, users, tasks


def create_tables(cursor):
    with open('create_tables.sql', 'r') as f:
        sql = f.read()
        cursor.execute(sql)


def populate_data(cursor):
    statuses, users, tasks = generate_data()

    cursor.executemany("INSERT INTO status(name) VALUES (%s);", statuses)

    cursor.executemany("INSERT INTO users(fullname, email) VALUES (%s, %s);", users)

    cursor.executemany(
        """
        INSERT INTO tasks(title, description, status_id, user_id) 
        VALUES (%s, %s, (SELECT id FROM status WHERE name = %s), (SELECT id FROM users WHERE email = %s));
        """, tasks
    )


def create_db():
    with psycopg2.connect(dbname="postgres", user="postgres", password="pass", host="localhost",
                          port="5432") as connection:
        cursor = connection.cursor()
        create_tables(cursor)
        populate_data(cursor)


if __name__ == "__main__":
    create_db()
