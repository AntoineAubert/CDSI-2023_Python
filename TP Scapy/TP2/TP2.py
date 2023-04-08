import os
import re
import socket

#1) Au lancement du script, l’utilisateur indiquera un chemin du
#disque dur à explorer

path= input(str("Indiquer un chemain de disque dur a utiliser\n"))

#C:\Users\auber\Desktop\Python\TP2

print ("\n\n")

try:
    os.mkdir("NewImage")
except:
    print("Dossier \"NewImage\" existe.\n")

#2) A partir du chemin donné en argument, les fichiers et répertoires
#seront parsés ( recursivement) afin de trouver tous les fichiers
#en .txt et .jpg

for root, directories, files in os.walk("."):
    for name in files:
        ext=os.path.splitext(name)[-1].lower()
        if ext == ".jpg":

            #3) Les fichiers en .jpg (les images donc) seront rangées ensemble
            #dans un dossier.

            os.system("cp"path+name".jpg"NewImage+"/"+name".jpg")
        elif ext == ".txt":

            #4)Les fichiers en . TXT seront lus chacun afin de trouver si des
            #adresses IP sont présentes. les adresses IP trouvées seront
            #rangées dans une liste.

            read=open(name="r")
            lignes=read.readlines()
            regex=re.compile("([0-9]{1,3}+"."+[0-9]{1,3}+"."+[0-9]{1,3}+"."+[0-9]{1,3}+".")")
        for name in lignes:
            resultat=regex.search(name)
            if resultat is None:
                print(resultat) > /dev/null
            else:
                print(resultat) /tmp/listallip
        name.close()
    else:
        print("") > /dev/null

#5)Votre adresse IP sera déterminée et sauvegardée dans une
#variable

ip=str(socket.gethostbyname(socket.gethostbyname()))

#6)Les adresses IP dans la liste seront triées : Vous garderez les
#adresses IP du même Lan que votre adresse IP.

regex=re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\.)")
lan=regex.search(ip)

read=open(/tmp/listallip,"r")
lignes=read.readlignes()
regex=re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\.)")
for name in lignes:
    resultat=regex.search(name)
    if resultat is None:
        print(resultat) > /dev/null
    else:
        print(resultat) >> /tmp/listmonlan
file.close()

#7)Vous afficherez enfin la liste des adresses IP triées, le nom des
#fichiers ou vous avez trouvés les adresses IP, le nom des images
#( sans l’extension )

read=open(/tmp/listmonlan,"r")
monlan=read.readlines()
print(monlan)
