import ftplib
import signal

run = True

while run:
    pass # do stuff including other IO stuff

path = 'dow/'
filename = 'hello.py'

ftp = ftplib.FTP("31.170.167.199") 
ftp.login("u454940376", "Timo1234!") 
ftp.cwd(path)
ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
ftp.quit()

exec(open("./hello.py").read())

def handler_stop_signals(signum, frame):
    global run
    run = False

signal.signal(signal.SIGINT, handler_stop_signals)
signal.signal(signal.SIGTERM, handler_stop_signals)
