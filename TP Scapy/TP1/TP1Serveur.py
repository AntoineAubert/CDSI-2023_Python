#import des differentes biblioteque
import socket
import random
s=socket.socket()
host='10.6.0.1' # a modifier en fonction de l'adresse ip de votre machine
port=2345
s.bind((host,port))
s.listen()
conn,addr=s.accept()

#declaration des differentes variable utilisé
essai=''
choixCouleur=""
bon=0
mal=0
faux=0

# La Focntion permet de genere un nombre aletoire pour recupere la couleur
def generation():
    for i in range(1,4):
        Dicco={"N":0,"R":1,"V":2,"J":3,"O":4,"B":5,"G":6,"W":7}
        nb=random.randint(0,7)
        choixCouleur=choixCouleur+Dicco[nb]
    return[choixCouleur]

#La fonction permet de recupere la data et d'indique le choix  bon mal faux...
def recup(data):
    for lettre in essai:
        
        i=0
        if lettre == choixCouleur[i]:
            bon=bon+1
        elif lettre in choixCouleur and lettre != choixCouleur [i]:
            mal=mal+1
        else:
            faux=faux+1
    return[bon,mal,faux]

#on arrive ici sur la fonction principal qui permet donc de renvoier ou non la data correcte ou fausse 
def mastermind(data):
    R=1
    z=1
    recup(data)
    while R==1:
        data=conn.recv(1024)
        data=(data.decode("utf8"))
        if(bon!=4):
            data=("Code incorrect ! sur vos 4 couleurs, vous en avez bien placées ", bon,", mal placées ", mal," et avez fait ", faux," erreurs".encode("utf8"))
            conn.send(data)
            recup(data)
            z=z+1
        else:
            data=("C'est gagné ! La combinaison était ", choixCouleur," ! Vous l'avez trouvé en ",z ,"coup(s) !".encode("utf8"))
            conn.send(data)
            data=("Fin".encode("utf8"))
            conn.send(data)
            R=0

#Ici le serveur permet de ce presente et de definir le jeux 
data=("Bonjour, je suis le serveur de jeu de mastermind.\r\n".encode("utf8"))
conn.send(data)

#on fait apple a la fonction generation pour genere la couleur
generation()

# on posse la question que le client doit repondre
data=("Je pense à une combinaison de 4 couleurs devine laquelle !".encode("utf8"))
conn.send(data)

data=conn.recv(1024)

mastermind(data)

data=conn.recv(1024)
data=data.decode("utf8")

conn.close()
s.close()