from repositories.pastry import Pastry


class DynamoDbPastryRepository:

    def __init__(self, dynamodb: "botocore.client.DynamoDb", table_name: str):
        self.dynamodb = dynamodb
        self.table_name = table_name

    def store(self, pastry: Pastry):
        self.dynamodb.put_item(TableName=self.table_name, Item={
            "type": {
                "S": pastry.type,
            },
            "amount": {
                "N": str(pastry.amount),
            }
        })
