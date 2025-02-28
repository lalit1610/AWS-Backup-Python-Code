import boto3
from botocore.exceptions import ClientError

def start_backup_job(instance_arn):
    client = boto3.client('backup', region_name='eu-west-1')  # Ensure the correct region

    try:
        response = client.start_backup_job(
            BackupVaultName='Default',
            ResourceArn=instance_arn,
            IamRoleArn='arn:aws:iam::412717554593:role/service-role/AWSBackupDefaultServiceRole',
        )
        print("Backup Job started:", response['BackupJobId'])
    except ClientError as e:
        if e.response['Error']['Code'] == 'InvalidParameterValueException':
            print("Resource belongs in another AWS region or incorrect ARN format.")
        else:
            print("Error starting backup job:", e)

def main():
    # Example instance ARN to back up
    example_instance_arn = 'arn:aws:ec2:eu-west-1:412717554593:instance/i-0025219a0f30b7b26'
    start_backup_job(example_instance_arn)

if __name__ == '__main__':
    main()
