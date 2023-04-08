def jourAnnee(prem,j,m,n):
    l=[] 
    j=j[prem:]+j[:prem]
    j=j*53
    for i in range(0,len(m)):
        for nbr in range(1,n[i]+1):
            l.append([m[i],nbr])
    for i in range(0,len(l)):
        l[i].append(j[i])
    return l

def determinationJour(nbr,mois,liste):
    for moi,nb,jour in liste:
#        print("nbr :",nbr," mois :",mois," moi:",moi," nb: ",nb," jour :",jour)
        if(nbr==nb and mois==moi):
            return jour
    return "rien"

def progPrincipal():
    Jours=["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]
    Mois= ["Janvier","Fevrier","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Decembre"]
    Nbr_j=[31,28,31,30,31,30,31,31,30,31,30,31]
    jour=input("quel est le premier jour de l'année 2021 ?")
    jour=jour.capitalize()
    ind=Jours.index(jour)
    liste=jourAnnee(ind,Jours,Mois,Nbr_j)
    nbr=int(input("Veuillez entrer le numero du jour\n"))
    mois=input("Veuillez entrer un mois\n")
    mois=mois.capitalize()
    j=determinationJour(nbr,mois,liste)
    print("le ",nbr," ",mois," est un ",j)

if(__name__=="__main__"):
    progPrincipal()