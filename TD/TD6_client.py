import socket
s=socket.socket()
host='10.6.4.125'
port=1234
s.connect((host,port))
data=s.recv(1024)
print(data.decode("utf8"))
s.send("Bonjour, je suis le Client".encode("utf8"))
while( data!="fin"):
    data=s.recv(1024)
    data=data.decode("utf8")
    print(data)
    mot=input("entrez un nombre")
    s.send(mot.encode("utf8"))
s.send("fin".encode("utf8"))
s.close()