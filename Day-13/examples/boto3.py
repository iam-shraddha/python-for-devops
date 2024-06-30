# Create s3 bucket
import boto3

client = boto3.client('s3')
                                                    
response = client.create_bucket(
    Bucket = ('monu_s3_bucket'),
)

# To get response from bucket
response = clien.get_bucket_acl(
    Bucket = ('monu_s3_bucket'),
)
print(response)
