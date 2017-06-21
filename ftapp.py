import boto3

conn = boto3.client('s3', region_name="eu-west-1", endpoint_url="https://ds31s3.swisscom.com", aws_access_key_id='5484335407854a4c9dc88e01206fc148/CF_P8_C2EF884E_EE05_4B55_A430_DAD9D9F9FE5E', aws_secret_access_key='xTTumTjwD1GCGZ+zyAzs9+pq+DE=',)
conn.create_bucket(Bucket="mytestbucket22")
