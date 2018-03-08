#!/bin/bash
#
#   RUN AS ROOT
#

cd /etc/ansible
wget -O ec2.py https://raw.githubusercontent.com/ansible/ansible/devel/contrib/inventory/ec2.py
wget -O ec2.ini https://raw.githubusercontent.com/ansible/ansible/devel/contrib/inventory/ec2.ini

# setup AWS Credentials Environment Variables
# this code assumes you only have one profile. if you have more 
# than one you will need to account for it in your export below.
export AWS_ACCESS_KEY_ID=`cat ~/.aws/credentials |grep id|awk '{print $3}'`
export AWS_SECRET_ACCESS_KEY=`cat ~/.aws/credentials |grep secret_access|awk '{print $3}'`
# Export for dynamic inventory
# http://docs.ansible.com/ansible/intro_dynamic_inventory.html#example-aws-ec2-external-inventory-script
export ANSIBLE_HOSTS=/etc/ansible/ec2.py
export EC2_INI_PATH=/etc/ansible/ec2.ini

