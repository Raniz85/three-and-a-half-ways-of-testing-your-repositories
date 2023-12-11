import psycopg

from repositories.pastry import Pastry
from repositories.psql_repository import PsqlPastryRepository


def test_that_psql_repository_stores_pastry_correctly():
    # Given a postgresql connection
    with psycopg.connect("dbname=test user=postgres password=postgres") as psql_connection:
        # Given a psql repository
        repo = PsqlPastryRepository(psql_connection)

        # and a pastry to store
        pastry = Pastry("Cinnamon Bun", 24)

        # When the pastry is stored
        repo.store(pastry)

        # Then the correct row exists in the database
        with psql_connection.cursor() as cursor:
            cursor.execute("SELECT EXISTS( SELECT 1 FROM pastry WHERE type = 'Cinnamon Bun' AND amount = 24)")
            assert cursor.fetchone()[0]
