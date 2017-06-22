from flask import Flask
import ftplib
import os
import boto3
import pandas as pd

app = Flask(__name__)

port = int(os.getenv("PORT"))

@app.route('/')
def hello_world():
    path = 'dow/'
    filename = 'segmentation.csv'
    ftp = ftplib.FTP("31.170.167.199") 
    ftp.login("u454940376", "Timo1234!") 
    ftp.cwd(path)
    ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
    filename = 'payment_details_aug.csv'
    ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
    ftp.quit()
    
    paymentsfile = 'payment_details_aug.csv'
    segmentsfile = 'segmentation.csv'
    outputfile = 'aggregated.csv'

    csv_payments = pd.read_csv(paymentsfile, dtype={'Company ID': float})
    csv_segments = pd.read_csv(segmentsfile, dtype={'Company ID': float})
    csv_payments = csv_payments.merge(csv_segments, on='Company ID')
    open(outputfile, 'a').close()
    csv_payments.to_csv(outputfile)
	
    conn = boto3.client('s3', region_name="eu-west-1", endpoint_url="https://ds31s3.swisscom.com", aws_access_key_id='5484335407854a4c9dc88e01206fc148/CF_P8_C2EF884E_EE05_4B55_A430_DAD9D9F9FE5E', aws_secret_access_key='xTTumTjwD1GCGZ+zyAzs9+pq+DE=',)
    conn.create_bucket(Bucket="mytestbucket22")
    filename = 'aggregated.csv'
    bucket_name = "mytestbucket22"
    conn.upload_file(filename, bucket_name, filename)
    return 'Hello, World!'

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=port)
