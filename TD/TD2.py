import random

def progPrincipal():
    nbr=int(input("Veuillez entrer le nombre maximum voulu :\n"))
    nbr_max=random.randint(1,nbr)
    nbr_u=0
    juste_prix(nbr_u,nbr_max)

def juste_prix(nbr_u,nbr_max):
    c=0
    while(nbr_u != nbr_max):
        nbr_u=int(input("Entrez un nombre :\n"))
        c=c+1
        if(nbr_u>nbr_max):
            print("Moins !\n")
        elif(nbr_u<nbr_max):
            print("Plus !\n")
    print("Vous avez gagné en ",c," coups !")


progPrincipal()
