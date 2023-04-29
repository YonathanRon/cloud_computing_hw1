import boto3
import time
# Create an EC2 client
ec2 = boto3.client('ec2')

# Set the parameters for the new instance
image_id = 'ami-00aa9d3df94c6c354'
instance_type = 't2.micro'
key_name = 'course-apr-29'
security_group_ids = ['sg-03608bebda3135d45']  # security group id of launch-wizard-5
subnet_id = 'subnet-0f7f309ec743dac6e'

# Launch the new instance
response = ec2.run_instances(
    ImageId=image_id,
    InstanceType=instance_type,
    KeyName=key_name,
    MinCount=1,
    MaxCount=1,
    SecurityGroupIds=security_group_ids,
    SubnetId=subnet_id,
)

security_group_id = 'sg-03608bebda3135d45'

# specify the port to open
port = 8000

# add inbound rule to security group
response_sec = ec2.authorize_security_group_ingress(
    GroupId=security_group_id,
    IpPermissions=[
        {
            'IpProtocol': 'tcp',
            'FromPort': port,
            'ToPort': port,
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0'
                },
            ]
        },
    ]
)

print(response)
# Print the ID of the new instance
instance_id = response['Instances'][0]['InstanceId']
print('Created instance with ID: ' + instance_id)

ec2_instance = response['Instances'][0]
ec2_instance.wait_until_running()

# Wait for the instance to be ready to use
print("Waiting for the instance to be ready...")
time.sleep(30)  # Wait for 30 seconds for the instance to fully initialize

print(f"Instance {instance_id} is now ready to use.")