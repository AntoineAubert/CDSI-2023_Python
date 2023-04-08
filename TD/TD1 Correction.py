def demandeUtilisateurs():
	age=int(input("Quel est votre age?\n"))
	poids=int(input("Quel est votre poids?\n"))
	taille=int(input("Quel est votre taille (en cm)?\n"))
	sexe=input("Quel est votre sexe ? (F ou H)\n")
	print("Quel est votre niveau d'activité ?\n")
	print("Sédentaire : 1\n")
	print("Trés faible activité :1.2\n")
	print("Activité légére : 1.4\n")
	print("Activité modérée : 1.6\n")
	print("Haute activité : 1.8\n")
	print("Activité extréme : 2\n")
	activite=float(input())
	attente=input("Voulez maigrif (m) ou grossir (g)?\n")
	return age,poids,taille,sexe,activite,attente

def calcul_BRM(age, poids,taille,sexe):
		if(sexe=="H"):
			BRM=66+(13.7 * poids) + (5 * taille)-(6.8 * age)
			return BRM
		elif(sexe=="F"):
			BRM=655+(9.6 * poids) + (1.7 * taille)-(4.7 * age)
			return BRM
		else:
			print("Vous n'avez pas entré F ou H\n")

def calcul_final(BRM,activite,attente):
	BRMa=BRM*activite
	if(attente=="m"):
		BRMf=BRMa*0.9
		return BRMf
	elif(attente=="g"):
		BRMf=BRMa*1.1
		return BRMf
	else:
		print("vous vous etes trompé entre m et g\n")

def progPrincipal():
	age,poids,taille,sexe,activite,attente=demandeUtilisateurs()
	BRM=calcul_BRM(age,poids,taille,sexe)
	print("Votre BRM est de : ",BRM, " Calories par jours")
	BRMf=calcul_final(BRM,activite,attente)
	print("Votre nombre de calories par jour doit être de ",BRMf)

progPrincipal()
