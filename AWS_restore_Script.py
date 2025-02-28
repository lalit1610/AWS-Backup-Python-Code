import boto3
from botocore.exceptions import ClientError

def restore_backup(recovery_point_arn):
    client = boto3.client('backup', region_name='eu-west-1')

    try:
        # Define necessary metadata for EC2 instance restoration
        metadata = {
            'InstanceType': 't2.micro',  # Correctly formatted instance type
            # Add other necessary metadata fields here if needed
        }

        # Start the restore job with the essential metadata
        response = client.start_restore_job(
            RecoveryPointArn=recovery_point_arn,
            IamRoleArn='arn:aws:iam::412717554593:role/service-role/AWSBackupDefaultServiceRole',
            Metadata=metadata
        )
        print("Restore Job started:", response['RestoreJobId'])
    except ClientError as e:
        if e.response['Error']['Code'] == 'InvalidParameterValueException':
            print("Invalid resource type or unsupported resource for restoration.")
        elif e.response['Error']['Code'] == 'InvalidRestoreMetadataException':
            print("Restore metadata is invalid. Please check the provided metadata fields and their values.")
        else:
            print("Error starting restore job:", e)

def main():
    example_recovery_point_arn = 'arn:aws:ec2:eu-west-1::image/ami-0757e937f504f1d92'
    restore_backup(example_recovery_point_arn)

if __name__ == '__main__':
    main()
