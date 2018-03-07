#!/usr/bin/env python3
import boto3

ec2 = boto3.client('ec2')
ec2rec = boto3.resource('ec2')
my_vpc = ec2.describe_vpcs()

#grab vpc id
vpc_id = my_vpc['Vpcs'][0]['VpcId']

sacpy_sec_group = ec2.create_security_group(
  Description='Demo security group for Sacramento Python User Group',
  GroupName='SacPyGroup',
  VpcId=vpc_id
)
print(sacpy_sec_group)

#create ingress rules for newly created 
ec2.authorize_security_group_ingress(
  CidrIp='0.0.0.0/0',
  FromPort=22,
  GroupId=sacpy_sec_group['GroupId'],
  IpProtocol='tcp',
  ToPort=22
)

#create a volume to attach to instance
volume_details=ec2.create_volume(
  AvailabilityZone='us-west-1b',
  Size=60,
  VolumeType='gp2',
  TagSpecifications=[
    {
      'ResourceType': 'volume',
      'Tags': [
        {
          'Key': 'Environment',
          'Value': 'Production'
        },
        {
          'Key': 'Purpose',
          'Value': 'Backup'
        }
      ]
    }
  ]
)
'''

Apply Ingress rules to security group

create volume object and device mapping for new EBS Volume

create hash table of tags

define linux ami

create reservation

apply tags 

'''