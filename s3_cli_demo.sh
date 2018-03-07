#!/bin/sh

export bucket_name='sac-py-demo-bucket'
export cli_bucket='sacpyclibucket'

#aws s3 cp notes.txt s3://${bucket_name}
aws s3 ls s3://${bucket_name}

aws s3api create-bucket --acl private --bucket $cli_bucket --region us-east-1

aws s3 rm s3://${cli_bucket}