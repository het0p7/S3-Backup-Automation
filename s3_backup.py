'''
Docstring for s3_backup

This is a script for taking backup from local to AWS S3
'''

import boto3

# specify Mumbai region
s3 = boto3.resource(
    "s3"
)

def show_bucket(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)

def create_bucket(s3,bucket_name,region):
    s3.create_bucket(
        Bucket=bucket_name,  # bucket name must be globally unique
        CreateBucketConfiguration={
            "LocationConstraint": region
        }
    )
    print("Bucket created successfully")

def upload_backup(s3,file_name,bucket_name,key_name):
    data = open(file_name,'rb')
    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
    print("backup Uploaded succesfully")



#create_bucket(s3)
bucket_name="python-demo-unique-126"
region="ap-south-1"
file_name = r"C:\Users\hetpa\OneDrive\Documents\Desktop\AI\backups\backup_2026-02-06.tar.gz"
bucket_name = "python-demo-unique-123"
upload_backup(s3,file_name,bucket_name,"my-backup.tar.gz")