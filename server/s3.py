import os
from dotenv import load_dotenv
import boto3
from botocore.exceptions import ClientError
import logging

load_dotenv()

AWS_ACCESS_KEY = os.environ['AWS_ACCESS_KEY']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
REGION = os.environ['REGION']
BUCKET_NAME = os.environ['BUCKET_NAME']


s3 = boto3.client(
  "s3",
  REGION,
  aws_access_key_id=AWS_ACCESS_KEY,
  aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

def upload_file(image_binary, file_name):
    """Upload a file to an S3 bucket

    :param image_binary: Image binary file to upload
    :param file_name: file_name. Will correspond to object key in S3
    :param bucket: Bucket to upload to
    :return: aws_image_src: URL to image in S3
    """



    # Upload the file
    try:
        # response = s3.upload_file(file_name, bucket, object_name)
        response = s3.put_object(
            Body=image_binary,
            Bucket=BUCKET_NAME,
            Key=file_name,
            ContentType='image/jpeg')

        aws_image_src = response.get_resource_url(BUCKET_NAME, file_name)
        print("upload_file", aws_image_src)

    except ClientError as e:
        logging.error(e)
        return

    return aws_image_src


# s3.download_file(BUCKET_NAME, 'indy.gif', 'newindy.gif')