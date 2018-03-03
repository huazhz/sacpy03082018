import boto3

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
  print(bucket.name)


'''

Create new bucket

write object to new bucket

list all objects in a bucket

sync files with a bucket

remove bucket

'''