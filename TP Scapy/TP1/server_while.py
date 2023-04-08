import socket
s=socket.socket()
host='10.6.5.33'
port=1234
s.bind((host,port))
s.listen()
conn,addr=s.accept()
print(addr)
conn.send("Bonjour, je suis le serveur".encode("utf8"))
data=conn.recv(1024)
print(data.decode("utf8"))
while( data!="fin"):
    mot=input("entrez un mot")
    conn.send(mot.encode("utf8"))
    data=conn.recv(1024)
    data=data.decode("utf8")
    print(data)
s.send("fin".encode("utf8"))
conn.close()
s.close()