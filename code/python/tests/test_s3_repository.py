from unittest.mock import MagicMock

from repositories.pastry import Pastry
from repositories.s3_repository import S3PastryRepository

BUCKET_NAME = "test-bucket"


def test_that_store_pastry_calls_s3_correctly():
    # Given a mock of the S3 client
    s3 = MagicMock()

    # and an S3 pastry repository
    repo = S3PastryRepository(s3, BUCKET_NAME)

    # and a pastry to store
    pastry = Pastry("Cinnamon Bun", 24)

    # When the pastry is stored in the repository
    repo.store(pastry)

    # Then a file with the contents 24 is stored at s3://test-bucket/Cinnamon Bun
    s3.put_object.assert_called_with(Bucket=BUCKET_NAME, Key="Cinnamon Bun", Body="24".encode())
