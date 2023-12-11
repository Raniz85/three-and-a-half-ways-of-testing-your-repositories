from psycopg import Connection

from repositories.pastry import Pastry


class PsqlPastryRepository:
    connection: Connection

    def __init__(self, connection: Connection):
        self.connection = connection
        self._create_table()

    def _create_table(self):
        with self.connection.cursor() as cursor:
            cursor.execute("CREATE TABLE IF NOT EXISTS pastry (id SERIAL PRIMARY KEY, type TEXT NOT NULL, amount INT NOT NULL)")

    def store(self, pastry: Pastry):
        with self.connection.cursor() as cursor:
            cursor.execute("INSERT INTO pastry (type, amount) VALUES (%s, %s)", (pastry.type, pastry.amount))