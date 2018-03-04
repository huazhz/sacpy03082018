import boto3

iamclient = boto3.client('iam')
new_users = ['Bob', 'Sara', 'Fred', 'John', 'Larry']
python_group = "NoPerms"

group_info = iamclient.get_group(GroupName=python_group)
print(group_info)

for user in new_users:
  iamclient.create_user(UserName=user)
  iamclient.add_user_to_group(
    GroupName=python_group,
    UserName=user
  )

for user in new_users:
  iamclient.remove_user_from_group(
    GroupName=python_group,
    UserName=user
  )
  iamclient.delete_user(UserName=user)
