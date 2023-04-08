#import des differentes bibliotheque
import socket
s=socket.socket()
host='10.6.0.1' #a modifier en fonction de l'adresse ip machine
port=2345 #a modifier 
s.connect((host,port))
data=s.recv(1024)
print(data.decode("utf8"))
#Envoie du text de presentation
s.send("Bonjour je suis le client".encode("utf8"))

#La fonction permet de demander au client les differeents parametre
def parametre():
    data=s.recv(1024)
    data=data.decode("utf8")
    nbcouleur=input("entrer le nombre de couleur souhaitée")
    proposition=input("entrer le nombre de proposition max")

#La fonction permert de renvoyer et de compare et de modifier le resultat
def envoiCouleur():
    data=s.recv(1024)
    data=data.decode("utf8")
    print(data)
    couleur=input("entrez des couleurs")
    s.send(couleur.encode("utf8"))



#La boucle permet ici au client d'envoyer et de recevoir la bonne reponce.
while( data!="fin"): 
    envoiCouleur()
s.send("fin".encode("utf8"))
s.close()