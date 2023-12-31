import psycopg
import pytest
from testcontainers.postgres import PostgresContainer

from repositories.pastry import Pastry
from repositories.psql_repository import PsqlPastryRepository


@pytest.fixture
def psql_connection():
    container = PostgresContainer("postgres:16", driver="psycopg")
    container.start()
    with psycopg.connect(container.get_connection_url().replace("+psycopg", "")) as connection:
        yield connection
    container.stop()


def test_that_psql_repository_stores_pastry_correctly(psql_connection):
    # Given a psql repository
    repo = PsqlPastryRepository(psql_connection)

    # and a pastry to store
    pastry = Pastry("Cinnamon Bun", 24)

    # When the pastry is stored
    repo.store(pastry)

    # Then it can be retrieved again
    assert repo.get("Cinnamon Bun") == pastry
