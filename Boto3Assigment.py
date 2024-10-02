import boto3
from botocore.exceptions import ClientError

def create_s3_bucket(bucket_name, region='us-west-2'):
    s3_client = boto3.client('s3', region_name=region)
    try:
        if region == 'us-west-2':
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        print(f"Bucket {bucket_name} created successfully.")
    except ClientError as e:
        print(e)

def launch_ec2_instance(key_name, security_group_id, instance_type='t2.micro', region='us-west-2'):
    ec2 = boto3.resource('ec2', region_name=region)
    
    instances = ec2.create_instances(
        ImageId='ami-0c55b159cbfafe1f0',  # Amazon Linux 2 AMI (You can replace with a different AMI if needed)
        MinCount=1,
        MaxCount=1,
        InstanceType=instance_type,
        KeyName=key_name,
        SecurityGroupIds=[security_group_id],
        UserData='''
        #!/bin/bash
        yum update -y
        yum install -y httpd
        systemctl start httpd
        systemctl enable httpd
        echo "<html><h1>Welcome to My Web Application</h1></html>" > /var/www/html/index.html
        ''',  # This script installs and configures Apache
    )

    for instance in instances:
        print(f"Launched EC2 Instance with ID: {instance.id}")

# Example Usage
create_s3_bucket('mandarphadkedevops', region='us-west-2')

