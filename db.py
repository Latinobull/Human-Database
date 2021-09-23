import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")


class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            f"dbname='humans' user={USER} password='{PASSWORD}' host='localhost' port='5432'"
        )

        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS human (id SERIAL PRIMARY KEY, name text, age integer, job text, salary money, bank money  )"
        )
        self.conn.commit()

    def insert(self, name, age, job, salary, bank):
        self.cur.execute(
            "INSERT INTO human (name, age, job, salary, bank) VALUES (%s,%s,%s,%s,%s)",
            (name, age, job, salary, bank),
        )
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM human")
        rows = self.cur.fetchall()
        return rows

    def viewName(self):
        self.cur.execute("SELECT id, name FROM human")
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM human WHERE id = %s", (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
