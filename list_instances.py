#!/usr/bin/python3
import boto3

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

Ids = []
for instance in ec2.instances.all():
    Ids.append(instance.id)

#Start and stopping instances

client.start_instances(InstanceIds=Ids)

client.stop_instances(InstanceIds=Ids)
