import boto3

s3 = boto3.resource('s3')
client = boto3.client('s3')
bucket_name = 'sac-py-demo-bucket'

for bucket in s3.buckets.all():
  print(bucket.name)

s3.create_bucket(
  ACL='public-read',
  Bucket=bucket_name,
  CreateBucketConfiguration={
    'LocationConstraint': 'us-west-1'
  }
)

s3.meta.client.upload_file('demo.json', bucket_name, 'demo.json')

client.list_objects(
  Bucket=bucket_name
)
'''

sync files with a bucket

remove bucket

'''