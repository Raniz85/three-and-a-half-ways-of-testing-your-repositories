from repositories.pastry import Pastry


class S3PastryRepository:

    def __init__(self, s3: 'botocore.client.S3', bucket_name: str):
        self.s3 = s3
        self.bucket_name = bucket_name

    def store(self, pastry: Pastry):
        self.s3.put_object(Bucket=self.bucket_name, Key=pastry.type, Body=str(pastry.amount).encode())

