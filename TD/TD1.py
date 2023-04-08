age= int( input ("Pouvez-vous nous donner votre l’âge.\n")) 
poids= float (input ("votre poids en KG.\n"))
taille = float (input ("votre taille en cm\n"))
sexe= (input("votre sexe.\n"))

if (sexe=="h"):
    brm=66+(13.7*poids)+(5*taille)-(6.8*age)
    print(brm)
elif(sexe=="f"):
    brm=655+(poids*9.6)+(1.7*taille)-(4.7*age)
    print(brm)
else:
    print("Vous n'avez pas reussi")


activite= float(input("Votre type d'activité\n"
"Sédentaire = 1\n"
"Très faible activité = 1.2\n"
"Activité légère = 1.4\n"
"Activité modérée = 1.6\n"
"Haute activité = 1 .8\n"
"Activité extrême = 2\n"))
brma=brm*activite
print(brma)

conportement=input("Voulez vous maigrir ou grossir \n")
if (conportement=="m"):
    brma= brma-brma*0.1
    print(brma)
elif(conportement=="g"):
    brma = brma+brma*0.1
    print(brma)
