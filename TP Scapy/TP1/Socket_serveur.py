import socket
host="10.4.218.74"
port=1337
s=socket.socket()
s.bind((host,port))
s.listen()
s_client,adresse=s.accept()
print("le port de connexion du client est :",adresse[1])
s_client.send("Je suis le serveur, bonjour Client".encode())
data=s_client.recv(64)
print(data.decode())
s_client.close()
s.close()