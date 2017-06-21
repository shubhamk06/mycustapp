from flask import Flask
import ftplib
import os
import boto3

app = Flask(__name__)

port = int(os.getenv("PORT"))

@app.route('/')
def hello_world():
    conn = boto3.client('s3', region_name="eu-west-1", endpoint_url="https://ds31s3.swisscom.com", aws_access_key_id='5484335407854a4c9dc88e01206fc148/CF_P8_C2EF884E_EE05_4B55_A430_DAD9D9F9FE5E', aws_secret_access_key='xTTumTjwD1GCGZ+zyAzs9+pq+DE=',)
    conn.create_bucket(Bucket="mytestbucket22")
    return 'Hello, World!'

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=port)
