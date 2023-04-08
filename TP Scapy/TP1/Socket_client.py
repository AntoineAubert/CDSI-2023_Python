import socket,time
host="10.4.218.74"
port=1337
s=socket.socket()#socket reseau ipv4, TCP
#s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)=> SOCK_DGRAM: UDP
s.connect((host,port))
data=s.recv(64)
print(data.decode())
s.send("je suis le client, au revoir".encode())
s.close()