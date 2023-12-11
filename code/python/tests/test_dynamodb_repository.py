import json

import httpretty
import boto3

from repositories.dynamodb_repository import DynamoDbPastryRepository
from repositories.pastry import Pastry

TABLE_NAME = "test-table"


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_that_store_pastry_calls_dynamodb_correctly():

    # Given a mock of the DynamoDB API
    httpretty.register_uri(
        httpretty.POST,
        "https://dynamodb.eu-north-1.amazonaws.com/",
        body='{}'
    )
    ddb = boto3.client("dynamodb", region_name="eu-north-1", aws_access_key_id="mykey", aws_secret_access_key="mysecret")

    # and an S3 pastry repository
    repo = DynamoDbPastryRepository(ddb, TABLE_NAME)

    # and a pastry to store
    pastry = Pastry("Cinnamon Bun", 24)

    # When the pastry is stored in the repository
    repo.store(pastry)

    # Then an item with values for type and amount is stored in the table
    body = json.loads(httpretty.last_request().body)
    assert body["TableName"] == TABLE_NAME
    assert body["Item"] == {
        "type": {
            "S": "Cinnamon Bun"
        },
        "amount" : {
            "N": "24"
        }
    }
