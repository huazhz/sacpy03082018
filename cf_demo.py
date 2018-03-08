#!/usr/bin/env python3
import boto3

template_name = '.\demo.json'

cf = boto3.client('cloudformation')

cf.create_stack(
  StackName='sacpydemo1',
  TemplateURL='https://s3-us-west-1.amazonaws.com/sac-py-demo-bucket/demo.json',
  Parameters=[
    {
      'ParameterKey': 'BucketName',
      'ParameterValue': 'sacpydemo1'
    },
    {
      'ParameterKey': 'AccessCTL',
      'ParameterValue': 'Private'
    }
  ]
)